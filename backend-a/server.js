const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 3001;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.json({
    message: 'Backend server is running!',
    port: PORT,
    timestamp: new Date().toISOString()
  });
});

app.get('/health', (req, res) => {
  res.json({
    status: 'ok'
  });
});

app.get('/api/status', (req, res) => {
  res.set('X-Backend', 'A');
  res.set('Cache-Control', 'max-age=60');

  res.json({
    status: 'online',
    uptime: process.uptime(),
    timestamp: new Date().toISOString(),
    success: true
  });
});

app.get('/api/data', (req, res) => {
  res.json({
    data: 'Sample data from backend A',
    success: true
  });
});

app.get('/api/cache', (req, res) => {
  res.set('X-Backend', 'A');
  res.set('Cache-Control', 'max-age=60');

  res.json({
    message: 'This response is cacheable',
    status: 'ok'
  });
});

app.post('/api/data', (req, res) => {
  const body = req.body;

  res.json({
    message: 'Data received by backend A',
    received: body,
    success: true
  });
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Backend A running on http://0.0.0.0:${PORT}`);
});
