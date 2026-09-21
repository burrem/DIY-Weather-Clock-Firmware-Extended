# V2.8.5

## Fixes and improvements

- Fixed compilation with newer ESP8266 Arduino Core versions where
  `ESP8266WebServer::client()` returns `WiFiClient` by value.
- The 48-hour pressure chart now works without Netatmo and records wttr.in
  pressure when Netatmo is disabled or unavailable.
- Netatmo remains the preferred pressure source when a valid reading is
  available.
- Imperial wttr.in pressure is normalized from inHg to hPa for history storage.
- The graph Y-axis now moves automatically for four-digit hPa scale labels while
  preserving all 96 half-hour samples.
- Renamed the web option from `Show 48-hour Netatmo chart` to
  `Show 48-hour pressure chart`.

Pressure history is stored in RAM and starts over after a reboot or OTA update.
