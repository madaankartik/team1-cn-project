# Computer Networks - Team 1

## Phase 1: Private Network Service Platform

This repository documents Phase 1 of a local Computer Networks project implemented across four macOS laptops on the same private LAN. The application path is:

```text
Client -> Private DNS -> HTTPS/TLS -> Nginx reverse proxy/load balancer -> Backend A or Backend B
```

The project demonstrates private DNS, HTTP/REST, TCP, TLS, HTTP caching, load balancing, and packet analysis.

## Team Members

| Machine | Team member | GitHub | Role |
| --- | --- | --- | --- |
| Mac 1 | Chirag Lalwani | [@lalwanichirag55](https://github.com/lalwanichirag55) | Private DNS server |
| Mac 2 | Arhan Alam | [@gitwitharhan](https://github.com/gitwitharhan) | Nginx edge, reverse proxy, and load balancer |
| Mac 3 | Arjun | [@Arjun421](https://github.com/Arjun421) | Backend A |
| Mac 4 | Kartik Madaan | [@madaankartik](https://github.com/madaankartik) | Backend B and test client |

## Architecture and Service Inventory

```text
Client
  |
  | DNS: app.team1.test / api.team1.test
  v
Mac 1 - dnsmasq (10.7.9.180)
  |
  | Both domains resolve to 10.7.19.111
  v
Mac 2 - Nginx edge (10.7.19.111)
  | HTTP :8080 | HTTPS :443 | TLS termination | load balancing
  +--------------------+
  |                    |
  v                    v
Mac 3                Mac 4
Backend A            Backend B
10.7.17.159:3001     10.7.24.251:3002
```

| Machine | IP address | Service | Port(s) |
| --- | ---: | --- | --- |
| Mac 1 | `10.7.9.180` | `dnsmasq` private DNS | `53` |
| Mac 2 | `10.7.19.111` | Nginx edge, reverse proxy, load balancer | HTTP `8080`, HTTPS `443` |
| Mac 3 | `10.7.17.159` | Backend A | `3001` |
| Mac 4 | `10.7.24.251` | Backend B | `3002` |

## Private DNS

Mac 1 runs `dnsmasq` with the following private DNS records:

```text
app.team1.test -> 10.7.19.111
api.team1.test -> 10.7.19.111
```

Verify name resolution from a client machine:

```bash
dig app.team1.test
dig api.team1.test
```

The final service must be accessed with its domain name rather than a backend IP address.

### Verified Mac 1 DNS Setup

```text
Software: dnsmasq
Configuration: /opt/homebrew/etc/dnsmasq.conf
Upstream resolver: 1.1.1.1
Port: 53
```

```bash
sudo dnsmasq --test
sudo brew services restart dnsmasq
sudo lsof -nP -iTCP:53 -iUDP:53
dig @10.7.9.180 app.team1.test
```

The verified lookup returns `10.7.19.111` from DNS server `10.7.9.180:53`.

## Run the Backends

### Backend A - Mac 3

```bash
cd backend-a
npm install
npm start
```

```text
Address: 10.7.17.159:3001
Response header: X-Backend: A
```

Backend A provides `GET /`, `GET /health`, `GET /api/status`, `GET /api/data`, `GET /api/cache`, and `POST /api/data`. All Backend A responses include `X-Backend: A`.

### Backend B - Mac 4

```bash
cd backend-b
python3 server.py
```

```text
Address: 10.7.24.251:3002
Endpoints: GET /, GET /api/status, GET /api/cache
Response header: X-Backend: B
```

Test Backend B locally:

```bash
curl -i http://127.0.0.1:3002/
curl -i http://127.0.0.1:3002/api/status
curl -i http://127.0.0.1:3002/api/cache
```

Test it from another LAN machine:

```bash
curl -i http://10.7.24.251:3002/api/status
```

## Nginx, Load Balancing, and TLS

Mac 2 is the only public edge entry point for clients. Nginx:

- Accepts HTTP on `8080` and HTTPS on `443`
- Terminates TLS for `app.team1.test`
- Proxies requests to Backend A (`10.7.17.159:3001`) and Backend B (`10.7.24.251:3002`)
- Load-balances repeated requests between the two backends

The active Nginx configuration is [`MAC2/nginx/edge-phase1.conf`](MAC2/nginx/edge-phase1.conf). It uses these certificate paths:

```text
/opt/homebrew/etc/nginx/ssl/app.team1.test.crt
/opt/homebrew/etc/nginx/ssl/app.team1.test.key
```

Verify and restart with:

```bash
sudo nginx -t
brew services restart nginx
curl -i https://app.team1.test/api/status
curl -i http://app.team1.test:8080/api/status
```

For the final Phase 1 demonstration, make repeated HTTPS requests to the private domain and show `X-Backend: A` and `X-Backend: B` in the responses. Mac 4 successfully verifies the issuing `Team1 Local Root CA` through the macOS System Keychain using `/usr/bin/curl`; configure the same trust on every client used during evaluation. Do not use `curl -k` in the demonstration.

## HTTP Caching

Backend B provides `GET /api/cache` for the caching requirement. Inspect the returned headers with:

```bash
curl -i http://10.7.24.251:3002/api/cache
```

Before the Phase 1 review, record the actual `Cache-Control` value and demonstrate a conditional request returning `304 Not Modified` using the Backend B `ETag`.

## Phase 1 Evidence Checklist

- [ ] Network topology diagram and IP/service inventory
- [ ] Ping reachability between all team machines
- [ ] DNS resolution evidence for both private domains
- [ ] Trusted HTTPS access through `app.team1.test`
- [ ] Repeated requests showing both `X-Backend: A` and `X-Backend: B`
- [ ] Wireshark evidence: DNS, TCP three-way handshake, TLS handshake, ports, and encrypted HTTPS data
- [ ] HTTP cache-header evidence and cache hit or `304` demonstration
- [ ] Required failure demonstrations: wrong DNS server, wrong DNS record, one backend stopped, both backends stopped, and wrong destination port

## Repository Structure

```text
MAC1/       Private DNS configuration and Mac 1 guide
MAC2/       Nginx TLS/load-balancer configuration and Mac 2 guide
MAC3/       Backend A owner guide
MAC4/       Backend B owner and test-client guide
backend-a/  Runnable Backend A source code
backend-b/  Runnable Backend B source code
config/     Shared Team 1 network inventory
docs/       Phase 1 setup order and evidence checklist
evidence/   Folder for screenshots and packet captures
```

Start with [`docs/phase1-setup.md`](docs/phase1-setup.md), then follow the README for the machine you own.

## Evaluator Access

This repository should be public or shared with the evaluator. It must contain complete backend source code, Nginx and DNS setup notes, and the screenshots/captures required as Phase 1 evidence.
