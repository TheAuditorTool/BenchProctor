// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00432(req, res) {
  const userInput = (await (await fetch("https://api.partner.example/v1/records")).json()).data || "";
  const [data] = String(userInput).split(',');
  const { drizzle } = require("drizzle-orm/better-sqlite3");
  const { sql } = require("drizzle-orm");
  const Database = require("better-sqlite3");
  const _drizzle = drizzle(new Database(":memory:"));
  await _drizzle.run(sql.raw("SELECT * FROM users WHERE id = '" + data + "'"));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00432 };
