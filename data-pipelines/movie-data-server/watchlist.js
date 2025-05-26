const path = require('path'); // ← definiera först
const express = require('express');
const cors = require('cors');
require('dotenv').config({ path: path.resolve(__dirname, '../env/watchlist.env') });
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

app.get('/random-movie', async (req, res) => {
    try {
      const result = await pool.query('SELECT * FROM watchlist ORDER BY RANDOM() LIMIT 1');
      res.json(result.rows[0]);
    } catch (err) {
      console.error('Database error:', err);
      res.status(500).send('Something went wrong');
    }
  });

app.get('/random-movie/:genre', async (req, res) => {
  const { genre } = req.params;

  try {
    const query = `
      SELECT *
      FROM watchlist
      WHERE LOWER(genres) LIKE '%' || LOWER($1) || '%'
      ORDER BY RANDOM()
      LIMIT 1
    `;
    const result = await pool.query(query, [genre]);
    res.json(result.rows[0]);
  } catch (err) {
    console.error('Database error:', err);
    res.status(500).send('Something went wrong');
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});