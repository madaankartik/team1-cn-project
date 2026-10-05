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
```

The private-key content is intentionally not stored in this repository.

## Verification commands

```bash
sudo nginx -t
brew services restart nginx
curl -i https://app.team1.test/api/status
```

The HTTPS test must succeed without `curl -k`, return `HTTP/1.1 200 OK`, and include `X-Backend: A` or `X-Backend: B`.
