// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00640(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const [data] = String(userInput).split(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const knex = require("knex");
  const _knex = knex({ client: "sqlite3", connection: { filename: ":memory:" }, useNullAsDefault: true });
  await _knex.raw("SELECT * FROM users WHERE id = '" + processed + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00640 };
