const express = require('express');
const app = express();
const pool = require('./db');

app.use(express.json());

app.get('/users', async (req, res) => {
    const { rows } = await pool.query('SELECT * FROM users');
    res.json(rows);
});

app.post('/users', async (req, res) => {
    const { name } = req.body;
    const { rows } = await pool.query('INSERT INTO users (name) VALUES ($1) RETURNING *', [name]);
    res.json(rows[0]);
});

app.listen(8000, () => console.log('Server running on port 8000'));
