# V2.7.3

## Reliable configuration page over WAN

- Reduced streamed HTTP chunk buffering so every generated chunk stays below
  the ESP8266 TCP MSS even when one appended HTML fragment crosses the threshold.
- Prevents malformed chunked encoding after short writes on slow or lossy paths.
- Fixed-length endpoints such as `/screen-data` are unchanged.
