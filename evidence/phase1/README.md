# Phase 1 Evidence

This directory stores Phase 1 verification evidence for the private LAN setup.

## Current evidence

```text
dns-verification.md
nginx-tls-verification.md
wireshark-screenshots/
terminal-output/
```

## Terminal output

Captured from Mac 3 (`10.7.17.159`) on 5 October 2026 with `/usr/bin/curl` (macOS System Keychain trust, no `-k`):

| File | Evidence shown |
|---|---|
| `terminal-output/01_ping.txt` | Mac 3 reaches Mac 1, Mac 2 and Mac 4 with 0% packet loss |
| `terminal-output/02_dns.txt` | System resolver is `10.7.9.180`; `app.team1.test` and `api.team1.test` resolve to `10.7.19.111` (authoritative) |
| `terminal-output/03_backends_direct.txt` | Backend A `:3001` returns `X-Backend: A`; Backend B `:3002` returns `X-Backend: B` |
| `terminal-output/04_https_tls.txt` | TLS 1.3 to `app.team1.test:443`, certificate issued by `Team1 Local Root CA`, `SSL certificate verify ok` |
| `terminal-output/05_load_balancing.txt` | 10 HTTPS requests alternate `X-Backend: A` / `X-Backend: B`; HTTP `:8080` edge also works |
| `terminal-output/07_ping_all_macs.txt` | Every Mac pings the other three with 0% packet loss |
| `terminal-output/08_nginx_t_mac2.txt` | `nginx -t` syntax OK on Mac 2 |
| `terminal-output/09_failure_wrong_port.txt` | Failure demo: port 9999 refused (TCP layer) while 443 works, with layer diagnosis |
| `terminal-output/06_cache_304.txt` | `Cache-Control: public, max-age=60`, ETags `"backend-a-v1"` / `"backend-b-v1"`, and `304 Not Modified` from both backends through the edge |

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
failure demos: wrong DNS server, wrong DNS record, one backend stopped, both backends stopped
```
