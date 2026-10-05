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

## Run the Backends

### Backend A - Mac 3

```text
Address: 10.7.17.159:3001
Run command: Pending confirmation from Backend A owner
```

Backend A must be LAN-accessible and provide `GET /`, `GET /api/status`, and an `X-Backend: A` response header, as required for the Phase 1 load-balancing demonstration.

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
- Terminates TLS for the private service domain
- Proxies requests to Backend A (`10.7.17.159:3001`) and Backend B (`10.7.24.251:3002`)
- Load-balances repeated requests between the two backends

For the final Phase 1 demonstration, make repeated HTTPS requests to the private domain and show `X-Backend: A` and `X-Backend: B` in the responses. The TLS certificate must be trusted by client machines; do not use `curl -k` in the demonstration.

## HTTP Caching

Backend B provides `GET /api/cache` for the caching requirement. Inspect the returned headers with:

```bash
curl -i http://10.7.24.251:3002/api/cache
```

Before the Phase 1 review, record the actual `Cache-Control` value and demonstrate a cache hit or a conditional request returning `304 Not Modified`, if supported by the endpoint.

## Phase 1 Evidence Checklist

- [ ] Network topology diagram and IP/service inventory
- [ ] Ping reachability between all team machines
- [ ] DNS resolution evidence for both private domains
- [ ] Trusted HTTPS access through `app.team1.test`
- [ ] Repeated requests showing both `X-Backend: A` and `X-Backend: B`
- [ ] Wireshark evidence: DNS, TCP three-way handshake, TLS handshake, ports, and encrypted HTTPS data
- [ ] HTTP cache-header evidence and cache hit or `304` demonstration
- [ ] Required failure demonstrations: wrong DNS server, wrong DNS record, one backend stopped, both backends stopped, and wrong destination port

## Evaluator Access

This repository should be public or shared with the evaluator. It must contain complete backend source code, Nginx and DNS setup notes, and the screenshots/captures required as Phase 1 evidence.
