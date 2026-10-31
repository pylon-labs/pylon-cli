use std::io::IsTerminal;
use std::sync::{Arc, Mutex};

use crate::auth::keyring_store::KeyringStore;
use crate::error::CliError;

pub(crate) struct SecretInputGuard {
    state: Option<Arc<Mutex<Option<HiddenTerminal>>>>,
}

impl SecretInputGuard {
    pub(crate) fn new() -> Result<Self, CliError> {
        if !std::io::stdin().is_terminal() {
            return Ok(Self { state: None });
        }
        let runtime = tokio::runtime::Handle::try_current().map_err(|_| hidden_input_error())?;
        #[cfg(unix)]
        let mut interrupt = tokio::signal::unix::signal(tokio::signal::unix::SignalKind::interrupt())
            .map_err(|_| hidden_input_error())?;
        #[cfg(unix)]
        let mut terminate = tokio::signal::unix::signal(tokio::signal::unix::SignalKind::terminate())
            .map_err(|_| hidden_input_error())?;
        #[cfg(windows)]
        let mut interrupt = tokio::signal::windows::ctrl_c().map_err(|_| hidden_input_error())?;

        let state = Arc::new(Mutex::new(Some(HiddenTerminal::new()?)));
        let on_interrupt = Arc::clone(&state);
        // Keep default interrupt termination through credential storage too,
        // after this guard restores the terminal and clears the shared state.
        drop(runtime.spawn(async move {
            #[cfg(unix)]
            let exit = tokio::select! {
                _ = interrupt.recv() => 130,
                _ = terminate.recv() => 143,
            };
            #[cfg(windows)]
            let exit = { interrupt.recv().await; 130 };
            #[cfg(not(any(unix, windows)))]
            let exit = 130;
            drop(on_interrupt.lock().unwrap_or_else(|p| p.into_inner()).take());
            std::process::exit(exit);
        }));
        Ok(Self { state: Some(state) })
    }
}

impl Drop for SecretInputGuard {
    fn drop(&mut self) {
        if let Some(state) = self.state.take() {
            drop(state.lock().unwrap_or_else(|p| p.into_inner()).take());
        }
    }
}

struct HiddenTerminal {
    #[cfg(unix)]
    _echo: Option<crate::profiles::commands::EchoOff>,
    #[cfg(windows)]
    saved: (usize, u32),
}

impl HiddenTerminal {
    fn new() -> Result<Self, CliError> {
        #[cfg(unix)]
        {
            let echo = crate::profiles::commands::EchoOff::new();
            if !echo.active() {
                return Err(hidden_input_error());
            }
            Ok(Self { _echo: Some(echo) })
        }
        #[cfg(windows)]
        {
            use windows_sys::Win32::System::Console::{GetStdHandle, STD_INPUT_HANDLE};
            // SAFETY: the borrowed standard input handle is not closed by this guard.
            Self::for_console(unsafe { GetStdHandle(STD_INPUT_HANDLE) })
        }
        #[cfg(not(any(unix, windows)))]
        Err(hidden_input_error())
    }

    #[cfg(windows)]
    fn for_console(handle: windows_sys::Win32::Foundation::HANDLE) -> Result<Self, CliError> {
        use windows_sys::Win32::Foundation::INVALID_HANDLE_VALUE;
        use windows_sys::Win32::System::Console::{GetConsoleMode, SetConsoleMode, ENABLE_ECHO_INPUT};
        if handle.is_null() || handle == INVALID_HANDLE_VALUE {
            return Err(hidden_input_error());
        }
        let mut saved = 0;
        // SAFETY: handle is borrowed; saved is writable and mode changes affect only this console.
        unsafe {
            if GetConsoleMode(handle, &mut saved) == 0
                || SetConsoleMode(handle, saved & !ENABLE_ECHO_INPUT) == 0
            {
                return Err(hidden_input_error());
            }
        }
        Ok(Self { saved: (handle as usize, saved) })
    }
}

#[cfg(windows)]
impl Drop for HiddenTerminal {
    fn drop(&mut self) {
        let (handle, mode) = self.saved;
        // SAFETY: restores the mode on the same borrowed console handle.
        unsafe { windows_sys::Win32::System::Console::SetConsoleMode(handle as _, mode); }
    }
}

fn hidden_input_error() -> CliError {
    CliError::Auth("Cannot hide terminal input; provide PYLON_TOKEN or pipe the token on stdin instead.".into())
}

#[derive(Debug)]
pub(crate) struct UnavailableCredentialStore;

impl KeyringStore for UnavailableCredentialStore {
    fn get(&self, _service: &str, _account: &str) -> Result<Option<String>, CliError> {
        Ok(None)
    }

    fn set(&self, _service: &str, _account: &str, _value: &str) -> Result<(), CliError> {
        Err(CliError::Auth("Cannot save credentials without a private config directory; use PYLON_TOKEN instead.".into()))
    }

    fn delete(&self, _service: &str, _account: &str) -> Result<(), CliError> {
        Ok(())
    }

    fn backend_label(&self) -> String {
        "unavailable (no private config directory)".into()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn unavailable_store_never_reads_or_persists_credentials() {
        let store = UnavailableCredentialStore;
        assert_eq!(store.get("pylon", "bearerAuth").unwrap(), None);
        assert!(store.set("pylon", "bearerAuth", "FAKE_TOKEN").is_err());
        assert!(store.delete("pylon", "bearerAuth").is_ok());
    }

    #[cfg(windows)]
    #[test]
    fn console_guard_rejects_invalid_handles() {
        use windows_sys::Win32::Foundation::INVALID_HANDLE_VALUE;
        assert!(HiddenTerminal::for_console(std::ptr::null_mut()).is_err());
        assert!(HiddenTerminal::for_console(INVALID_HANDLE_VALUE).is_err());
    }

    #[cfg(windows)]
    #[test]
    fn console_guard_hides_and_restores_input() {
        use windows_sys::Win32::Foundation::{CloseHandle, GENERIC_READ, GENERIC_WRITE, INVALID_HANDLE_VALUE};
        use windows_sys::Win32::Storage::FileSystem::{CreateFileW, FILE_SHARE_READ, FILE_SHARE_WRITE, OPEN_EXISTING};
        use windows_sys::Win32::System::Console::{AllocConsole, FreeConsole, GetConsoleMode, ENABLE_ECHO_INPUT};

        // Use a console input handle rather than the runner's piped stdin.
        unsafe {
            let allocated = AllocConsole() != 0;
            let name: Vec<u16> = "CONIN$\0".encode_utf16().collect();
            let handle = CreateFileW(name.as_ptr(), GENERIC_READ | GENERIC_WRITE,
                FILE_SHARE_READ | FILE_SHARE_WRITE, std::ptr::null(), OPEN_EXISTING, 0, std::ptr::null_mut());
            assert!(handle != INVALID_HANDLE_VALUE && !handle.is_null());
            let mut before = 0;
            assert_ne!(GetConsoleMode(handle, &mut before), 0);
            let guard = HiddenTerminal::for_console(handle).unwrap();
            let mut during = 0;
            assert_ne!(GetConsoleMode(handle, &mut during), 0);
            assert_eq!(during & ENABLE_ECHO_INPUT, 0);
            drop(guard);
            let mut after = 0;
            assert_ne!(GetConsoleMode(handle, &mut after), 0);
            assert_eq!(after, before);
            CloseHandle(handle);
            if allocated { FreeConsole(); }
        }
    }
}
