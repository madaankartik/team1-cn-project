# Phase 1 Setup Order

1. Connect all four Macs to the same private LAN and collect IP, gateway, interface, and MAC-address details.
2. Start Backend A on Mac 3 and Backend B on Mac 4.
3. Install and verify private DNS on Mac 1.
4. Generate and install the certificate and Nginx configuration on Mac 2.
5. Set Mac 1 and Mac 4 to use `10.7.9.180` as their DNS resolver.
6. Trust the edge certificate on every client Mac.
7. Verify DNS, HTTPS, load balancing, caching, and packet-capture evidence.

## Required Phase 1 Evidence

- Network inventory and topology diagram
- Ping results among all machines
- `dig` or `nslookup` output for both private domains
- Repeated edge requests showing `X-Backend: A` and `X-Backend: B`
- Wireshark captures of DNS, TCP handshake, TLS handshake, and ports
- Cache headers and cache hit or `304 Not Modified`
- Controlled failure evidence: bad DNS server, wrong record, one backend down, both backends down, and wrong port
