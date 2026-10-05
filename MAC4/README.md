# Mac 4 - Backend B and Test Client

**Owner:** Kartik Madaan

From the repository root:

```bash
cd backend-b
python3 server.py
```

Backend B listens on `0.0.0.0:3002` and returns `X-Backend: B`.

Verify:

```bash
curl -i http://10.7.24.251:3002/api/status
curl -i http://10.7.24.251:3002/api/cache
```
