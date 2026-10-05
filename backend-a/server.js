const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 3001;
const CACHE_ETAG = '"backend-a-v1"';

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use((req, res, next) => {
  res.set('X-Backend', 'A');
  next();
});

app.get('/', (req, res) => {
  res.json({
    message: 'Backend server is running!',
    backend: 'A',
    port: PORT,
    timestamp: new Date().toISOString()
  });
});

app.get('/health', (req, res) => {
  res.json({
    backend: 'A',
    status: 'ok'
  });
});

app.get('/api/status', (req, res) => {
  res.set('Cache-Control', 'no-store');

  res.json({
    backend: 'A',
    status: 'online',
    uptime: process.uptime(),
    timestamp: new Date().toISOString(),
    success: true
  });
});

app.get('/api/data', (req, res) => {
  res.json({
    backend: 'A',
    data: 'Sample data from backend A',
    success: true
  });
});

app.get('/api/cache', (req, res) => {
  res.set('Cache-Control', 'public, max-age=60');
  res.set('ETag', CACHE_ETAG);

  const clientEtags = String(req.get('If-None-Match') || '')
    .split(',')
    .map((value) => value.trim().replace(/^W\//, ''));

  if (clientEtags.includes(CACHE_ETAG) || clientEtags.includes('*')) {
    res.status(304).end();
    return;
  }

  res.json({
    backend: 'A',
    message: 'This response is cacheable',
    status: 'ok'
  });
});

app.post('/api/data', (req, res) => {
  const body = req.body;

  res.json({
    message: 'Data received by backend A',
    backend: 'A',
    received: body,
    success: true
  });
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Backend A running on http://0.0.0.0:${PORT}`);
});
