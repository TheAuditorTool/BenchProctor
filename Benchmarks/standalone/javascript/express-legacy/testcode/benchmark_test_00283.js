// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00283(req, res) {
  const userInput = req.query.id || "";
  const data = userInput != null ? userInput : '';
  const { drizzle } = require("drizzle-orm/better-sqlite3");
  const { sql } = require("drizzle-orm");
  const Database = require("better-sqlite3");
  const _drizzle = drizzle(new Database(":memory:"));
  await _drizzle.all(sql.raw("SELECT id, name FROM users WHERE name = '" + data + "'"));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00283 };
