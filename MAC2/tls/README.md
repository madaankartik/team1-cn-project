# TLS Certificate Material

This directory documents the public TLS setup for Phase 1.

Committed files:

- `openssl-san.cnf`: OpenSSL SAN configuration for `app.team1.test`, `api.team1.test`, and Mac 2 IP `10.7.19.111`.
- `team1-rootCA.crt`: public root CA certificate to install on client machines.

Private keys are intentionally not committed.

## Certificate generation commands

Run these on Mac 2 if the certificates need to be regenerated:

```bash
mkdir -p /opt/homebrew/etc/nginx/ssl

openssl genrsa -out /opt/homebrew/etc/nginx/ssl/team1-rootCA.key 2048

openssl req -x509 -new -nodes \
  -key /opt/homebrew/etc/nginx/ssl/team1-rootCA.key \
  -sha256 -days 3650 \
  -subj "/C=IN/O=Team1 CN Project/CN=Team1 Local Root CA" \
  -out /opt/homebrew/etc/nginx/ssl/team1-rootCA.crt

openssl genrsa -out /opt/homebrew/etc/nginx/ssl/app.team1.test.key 2048

openssl req -new \
  -key /opt/homebrew/etc/nginx/ssl/app.team1.test.key \
  -out /opt/homebrew/etc/nginx/ssl/app.team1.test.csr \
  -config MAC2/tls/openssl-san.cnf

openssl x509 -req \
  -in /opt/homebrew/etc/nginx/ssl/app.team1.test.csr \
  -CA /opt/homebrew/etc/nginx/ssl/team1-rootCA.crt \
  -CAkey /opt/homebrew/etc/nginx/ssl/team1-rootCA.key \
  -CAcreateserial \
  -out /opt/homebrew/etc/nginx/ssl/app.team1.test.crt \
  -days 825 -sha256 \
  -extensions req_ext \
  -extfile MAC2/tls/openssl-san.cnf
```

## Verification

```bash
openssl x509 -in /opt/homebrew/etc/nginx/ssl/app.team1.test.crt -noout -issuer -subject
```

Expected issuer:

```text
C=IN, O=Team1 CN Project, CN=Team1 Local Root CA
```

Expected subject:

```text
C=IN, O=Team1 CN Project, CN=app.team1.test
```
