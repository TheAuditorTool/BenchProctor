// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00291(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const data = `${userInput}`;
  const knex = require("knex");
  const _knex = knex({ client: "sqlite3", connection: { filename: ":memory:" }, useNullAsDefault: true });
  await _knex.raw("SELECT * FROM users WHERE id = '" + data + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00291 };
