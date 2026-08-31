# V2.7.0

## Localized city title

- Added an optional `Display city` field for an OLED-only localized city name.
- The original `City` remains the stable wttr.in lookup value.
- Russian city names use the compact Cyrillic font and are centered safely.
- The display-only name is applied and persisted without rebooting.
- Existing configurations fall back to the original city when the new field is empty.
