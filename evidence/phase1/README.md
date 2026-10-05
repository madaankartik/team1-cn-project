# Phase 1 Evidence

This directory stores Phase 1 verification evidence for the private LAN setup.

## Current evidence

```text
dns-verification.md
nginx-tls-verification.md
terminal-output/
screenshots/
wireshark-screenshots/
```

## Terminal output

Captured on 5 October 2026. All HTTPS requests use `/usr/bin/curl` with macOS System Keychain trust and no `-k`.

| File | Captured on | Evidence shown |
|---|---|---|
| `terminal-output/01_ping.txt` | Mac 3 | Mac 3 reaches Mac 1, Mac 2 and Mac 4 with 0% packet loss |
| `terminal-output/02_dns.txt` | Mac 3 | System resolver is `10.7.9.180`; `app.team1.test` and `api.team1.test` resolve to `10.7.19.111` (authoritative) |
| `terminal-output/03_backends_direct.txt` | Mac 3 | Backend A `:3001` returns `X-Backend: A`; Backend B `:3002` returns `X-Backend: B` |
| `terminal-output/04_https_tls.txt` | Mac 3 | TLS 1.3 to `app.team1.test:443`, certificate issued by `Team1 Local Root CA`, `SSL certificate verify ok` |
| `terminal-output/05_load_balancing.txt` | Mac 3 | 10 HTTPS requests alternate `X-Backend: A` / `X-Backend: B`; HTTP `:8080` edge also works |
| `terminal-output/06_cache_304.txt` | Mac 3 | `Cache-Control: public, max-age=60`, ETags `"backend-a-v1"` / `"backend-b-v1"`, and `304 Not Modified` from both backends through the edge |
| `terminal-output/07_ping_all_macs.txt` | All four Macs | Every Mac pings the other three with 0% packet loss (summary lines of each owner's output) |
| `terminal-output/08_nginx_t_mac2.txt` | Mac 2 | `nginx -t` syntax OK |
| `terminal-output/09_failure_wrong_port.txt` | Mac 2 | Failure demo: port 9999 refused (TCP layer) while 443 works, with layer diagnosis |
| `terminal-output/10_failure_dns.txt` | Mac 3 | Failure demo: wrong DNS server (timeout / NXDOMAIN) and missing record, with layer diagnosis |
| `terminal-output/11_failure_backend_a_down.txt` | Mac 3 | Failure demo: Backend A stopped, 6/6 HTTPS requests still 200 from Backend B, A restored and load balancing resumes |

## Terminal screenshots

| File | Evidence shown |
|---|---|
| `screenshots/mac2-https-verify-and-wrong-port.png` | Mac 2: `curl -v https://app.team1.test:443` with `SSL certificate verify ok`, then port `9999` refused |

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

## Evidence status

All Phase 1 evidence items are captured.
