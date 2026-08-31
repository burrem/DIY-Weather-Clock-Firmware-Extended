# V2.3.2

## Netatmo TLS reliability fix

- Reduced the non-MFLN Netatmo TLS receive buffer from 16 KB to 8 KB so it fits
  the ESP-01 heap after startup.
- Added readable connection-error and free-heap diagnostics for negative HTTP
  return codes.
- Retains all V2.3.1 pressure-chart layout improvements.
