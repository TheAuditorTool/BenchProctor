// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00720(req, res) {
  const userInput = req.headers.authorization || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const { drizzle } = require("drizzle-orm/better-sqlite3");
  const { sql } = require("drizzle-orm");
  const Database = require("better-sqlite3");
  const _drizzle = drizzle(new Database(":memory:"));
  await _drizzle.run(sql.raw("SELECT * FROM users WHERE id = '" + data + "'"));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00720 };
