# Wireshark Screenshots

These screenshots provide Phase 1 packet-level evidence for DNS, TCP, and TLS.

Key verified items:

- DNS traffic uses Mac 1 DNS server `10.7.9.180`.
- `app.team1.test` resolves to Mac 2 Nginx edge server `10.7.19.111`.
- HTTPS traffic reaches Mac 2 on TCP port `443`.
- TCP handshake packets are visible using `SYN`, `SYN, ACK`, and `ACK`.
- TLS handshake traffic is visible, including `Client Hello` with SNI `app.team1.test`.
- Encrypted TLS application data appears after the handshake.
