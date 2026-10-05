#!/usr/bin/env bash
set -euo pipefail

mkdir -p tls/out
openssl req -x509 -newkey rsa:2048 -nodes -sha256 -days 365 \
  -keyout tls/out/team1-server.key \
  -out tls/out/team1-server.crt \
  -subj '/CN=app.team1.test' \
  -addext 'subjectAltName=DNS:app.team1.test,DNS:api.team1.test'
