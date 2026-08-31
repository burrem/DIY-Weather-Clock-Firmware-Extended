# V2.7.4

## Acknowledged HTTP streaming

- Withdraws the ineffective V2.7.3 small-chunk workaround.
- Enables ESP8266 synchronous TCP writes for streamed/chunked responses.
- A new HTTP chunk is not started until the previous write is acknowledged.
- Fixed-length endpoints such as `/screen-data` remain unchanged.
