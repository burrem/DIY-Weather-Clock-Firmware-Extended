# V2.7.5

## Faster reliable HTTP streaming

- Queues each complete HTTP chunk (size, body and terminator) before waiting for ACK.
- Retries partial TCP writes and stops the connection instead of emitting a malformed next chunk.
- Waits for one acknowledgement per complete chunk, avoiding delayed-ACK pauses between tiny writes.
