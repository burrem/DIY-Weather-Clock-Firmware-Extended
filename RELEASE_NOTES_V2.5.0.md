# V2.5.0

## Live web screen

- Added `/screen`, a browser view of the physical 128x64 OLED.
- The page polls once per second and renders a pixel-perfect enlarged Canvas.
- Added `/screen-data`, which streams the existing 1024-byte SSD1306 framebuffer
  without allocating a duplicate frame on the ESP-01.
- Added a **Live screen** button to the configuration page.
- The viewer is intended for the local network or access through a trusted VPN;
  the ESP web server must not be exposed directly to the Internet.
