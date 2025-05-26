const path = require('path');
const express = require('express');
const cors = require('cors');
require('dotenv').config({ path: path.resolve(__dirname, '../env/whoop.env') });
const { Pool } = require('pg');

const app = express();
app.use(cors());
const port = 3000;

const pool = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: process.env.DB_NAME,
  password: process.env.DB_PASSWORD,
  port: process.env.DB_PORT,
});

app.get('/training-data', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM daily_summary');
    res.json(result.rows);
  } catch (err) {
    console.error('Database error:', err);
    res.status(500).send('Something went wrong');
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});