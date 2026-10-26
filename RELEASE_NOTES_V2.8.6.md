# V2.8.6

## Stability fixes

- Addressed the most likely cause of periodic reboots (typically within one or
  two days). Every HTTPS request (Netatmo, update check) allocated a 6 KB BearSSL
  stack; once the heap became fragmented the core could not find a 6 KB block and
  called `abort()`. The stack is now allocated once at boot and kept.
- Netatmo requests and the firmware update check are skipped, with a log entry,
  when the heap is too small for a TLS connection. A skipped update check is
  retried after an hour.

## Pressure history

- The 48-hour pressure history is mirrored to RTC memory. It now survives crashes,
  reboots and OTA updates, and only starts over after a power loss.
- History older than 48 hours without a new sample is discarded.
- Fixed spikes in the chart when Netatmo is enabled: a failed Netatmo request no
  longer records the wttr.in pressure (which typically differs from the station
  by several hPa). The sample is skipped and the next Netatmo reading is used.
  wttr.in still feeds the history when Netatmo is disabled.

## Diagnostics

- The boot log records the reset reason and, after a crash, the exception cause,
  address, uptime and heap state saved at the moment of the crash.
- `/log` starts with a status header: version, uptime, reset reason, the previous
  crash and the current/minimum free heap and largest free block.
- Heap usage is logged before every weather update and TLS request.
- An activity trail in RTC memory records what the firmware is doing (main loop,
  web server, OLED drawing, wttr.in, Netatmo, update check, EEPROM write) and the
  uptime, refreshed every second. After any reset, including a hardware watchdog
  that leaves no crash record, `/log` shows the last activity and uptime.
- `/log` also keeps the boot ROM's exception/watchdog details in its header, so
  they are not lost when the log buffer wraps.

## Build

- The PlatformIO build no longer forces unused float `printf`/`scanf` support into
  the image (`tools/strip_float_printf.py`). The firmware is ~7 KB smaller than
  it would otherwise be and stays below the ~512 KB OTA image limit.
