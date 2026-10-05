# Nginx and TLS Verification - Mac 2

## Active upstream servers

```text
Backend A: 10.7.17.159:3001
Backend B: 10.7.24.251:3002
```

## Certificate paths

```text
Certificate: /opt/homebrew/etc/nginx/ssl/app.team1.test.crt
Private key: /opt/homebrew/etc/nginx/ssl/app.team1.test.key
Public CA: MAC2/tls/team1-rootCA.crt
```

The private-key content is intentionally not stored in this repository.

## Verification commands

```bash
sudo nginx -t
brew services restart nginx
/usr/bin/curl -i https://app.team1.test/api/status
```

## Verified result - Mac 4

Mac 4 trusts `Team1 Local Root CA` through the macOS System Keychain. The successful trusted request used the built-in macOS curl client:

```text
HTTP/1.1 200 OK
Server: nginx/1.31.6
Content-Type: application/json
X-Backend: B

{"backend": "B", "status": "ok"}
```

This test used neither `-k` nor `--cacert`. The Conda/Homebrew curl client may use a separate CA bundle; `/usr/bin/curl` verifies against the macOS System Keychain.
