# V2.7.2

## DHCP/GPS NTP priority

- Starts SNTP before connecting Wi-Fi, matching the ESP8266 reference sequence.
- DHCP option 42 can now replace the primary public NTP server after association.
- Public NTP servers remain in use when DHCP supplies no server.
- The SNTP callback continues to log the resulting server list and reachability.
