# V2.8.3

## Size audit and weather diagnostics

- Restores compact successful wttr.in logging with temperature, condition,
  humidity, wind, pressure and WWO condition code.
- Logs dawn, sunrise, sunset and dusk whenever those fields are requested.
- Disables the unused built-in Adafruit SSD1306 splash image at compile time.
- Removes the unused WiFiUDP object and its linked implementation.
- Fixes the sun-data request counter so those values are refreshed every fourth
  weather request as intended.
