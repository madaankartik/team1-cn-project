# Mac 2 - Nginx Edge, TLS, and Load Balancer

**Owner:** Arhan Alam

1. Install Nginx and OpenSSL.
2. Generate the certificate from the repository root:

```bash
MAC2/tls/make-certs.sh
```

3. Copy the generated certificate and key to the paths configured in `nginx/edge-phase1.conf`.
4. Install that Nginx server configuration and reload Nginx.
5. Verify repeated HTTPS requests reach both backends:

```bash
curl -i https://app.team1.test/api/status
```

Clients must trust the certificate before the final demonstration. Do not use `curl -k` in the demo.
