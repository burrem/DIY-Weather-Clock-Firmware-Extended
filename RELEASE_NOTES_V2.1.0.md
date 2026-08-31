# V2.1.0

## What's new

- Added an optional 24-hour Netatmo barometric pressure trend screen.
- Stores 96 readings at 15-minute intervals in RAM and renders 48 half-hour bars.
- Shows the current pressure and the change since the oldest available reading.
- Added a web-portal option to include the trend screen in the display rotation.
- Shortened the compact OLED pressure suffix from `mmHg` to `mm`, preventing the
  descender of the final `g` from being clipped on the bottom display row.

## Notes

- Pressure history fills while the clock is running and resets after a reboot.
- The trend screen appears after the first successful Netatmo pressure reading.
- Existing saved configurations remain compatible; the new screen is disabled by
  default.
