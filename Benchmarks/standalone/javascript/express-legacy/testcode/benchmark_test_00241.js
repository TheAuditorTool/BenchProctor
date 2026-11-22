// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00241(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = Buffer.from(userInput, "base64").toString();
  const _coerced = parseInt(String(data), 10);
  const parsedId = _coerced;
  const { drizzle } = require("drizzle-orm/better-sqlite3");
  const { sql } = require("drizzle-orm");
  const Database = require("better-sqlite3");
  const _drizzle = drizzle(new Database(":memory:"));
  await _drizzle.all(sql.raw("SELECT id, name FROM users WHERE name = '" + parsedId + "'"));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00241 };
