# Phase 1 Evidence

This directory stores Phase 1 verification evidence for the private LAN setup.

## Current evidence

```text
dns-verification.md
nginx-tls-verification.md
wireshark-screenshots/
```

## Wireshark screenshots

The `wireshark-screenshots/` directory contains packet-level evidence for:

| File | Evidence shown |
|---|---|
| `01-arp-tcp-overview.jpeg` | LAN packet capture overview with ARP/TCP traffic |
| `02-dns-traffic-mac1-filter.jpeg` | DNS traffic involving Mac 1 DNS server `10.7.9.180` |
| `03-dns-app-team1-response.jpeg` | DNS response resolving `app.team1.test` to `10.7.19.111` |
| `04-dns-upstream-queries.jpeg` | DNS forwarding/upstream traffic to `1.1.1.1` |
| `05-tcp-handshake-443.jpeg` | TCP three-way handshake to Mac 2 HTTPS port `443` |
| `06-tcp-tls-session-443.jpeg` | TLS session traffic between client and Mac 2 |
| `07-tls-session-retransmission-view.jpeg` | Continued TCP/TLS traffic on port `443` |
| `08-tls-application-data.jpeg` | Encrypted TLS application data after handshake |
| `09-tls-sni-app-team1.jpeg` | TLS Client Hello with SNI `app.team1.test` |
| `10-repeat-tls-session.jpeg` | Additional HTTPS/TLS session traffic to Mac 2 |

## Evidence still expected for final demonstration

Add screenshots or terminal outputs for the remaining final demo items when available:

```text
network-inventory-and-ping-results
load-balancing-x-backend-a-and-b
cache-control-or-304-response
failure-demonstrations
```
