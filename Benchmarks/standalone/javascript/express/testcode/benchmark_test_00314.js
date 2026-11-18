// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00314(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const knex = require("knex");
  const _knex = knex({ client: "sqlite3", connection: { filename: ":memory:" }, useNullAsDefault: true });
  await _knex.raw("SELECT * FROM users WHERE id = '" + data + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00314 };
