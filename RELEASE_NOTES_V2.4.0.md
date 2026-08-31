# V2.4.0

## Detailed pressure line chart

- Replaced hourly bars with a line through all 96 fifteen-minute samples.
- Each sample occupies one horizontal pixel, spanning x=25 through x=120.
- The trace is two pixels thick vertically for OLED readability.
- A 3x3 marker identifies the newest pressure reading.
- MIN, MAX and delta continue to use the original samples.
