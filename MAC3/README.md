# Mac 3 - Backend A

**Owner:** Arjun

From the repository root:

```bash
cd backend-a
npm install
npm start
```

Backend A listens on `0.0.0.0:3001` and returns `X-Backend: A` on all routes.

Verify:

```bash
curl -i http://10.7.17.159:3001/api/status
```
