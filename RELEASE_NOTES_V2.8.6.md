# V2.8.6

- **Fewer reboots.** Fixed the most likely cause of the clock rebooting every
  day or two (running out of memory during HTTPS requests).
- **Pressure chart survives reboots and OTA updates.** It only starts over after
  a power loss.
- **No more spikes in the pressure chart** when a Netatmo request fails.
- **Better diagnostics in `/log`:** reset reason, last crash details, memory
  state and what the clock was doing before a reset.
- **Smaller firmware image** when built with PlatformIO.
