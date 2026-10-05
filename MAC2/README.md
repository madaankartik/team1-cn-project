# Mac 2 - Nginx Edge, TLS, and Load Balancer

**Owner:** Arhan Alam

1. Use `nginx/nginx.conf` as the full project Nginx configuration. `nginx/edge-phase1.conf` contains the same upstream/server blocks as a reusable fragment.
2. Keep the trusted certificate and private key at these paths:

```text
Certificate: /opt/homebrew/etc/nginx/ssl/app.team1.test.crt
Private key:  /opt/homebrew/etc/nginx/ssl/app.team1.test.key
```

3. Test and restart Nginx:

```bash
sudo nginx -t -c /opt/homebrew/etc/nginx/nginx.conf
brew services restart nginx
```

For a configuration-only reload:

```bash
sudo nginx -s reload
```

4. Verify HTTPS reaches either backend:

```bash
curl -i https://app.team1.test/api/status
```

The expected response is `HTTP/1.1 200 OK`, a JSON payload, and either `X-Backend: A` or `X-Backend: B`. Install the issuing CA certificate (or the self-signed server certificate) in each client Mac's trust store before testing; do not use `curl -k`.

TLS generation notes and the public root CA certificate are in `tls/`. Private keys are intentionally not committed.

Optional HTTP edge check:

```bash
curl -i http://app.team1.test:8080/api/status
```
