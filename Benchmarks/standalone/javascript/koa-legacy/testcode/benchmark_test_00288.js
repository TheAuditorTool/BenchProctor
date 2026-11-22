// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00288 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = Buffer.from(userInput, "base64").toString();
  const _coerced = parseInt(String(data), 10);
  const parsedId = _coerced;
  const { drizzle } = require("drizzle-orm/better-sqlite3");
  const { sql } = require("drizzle-orm");
  const Database = require("better-sqlite3");
  const _drizzle = drizzle(new Database(":memory:"));
  await _drizzle.all(sql.raw("SELECT id, name FROM users WHERE name = '" + parsedId + "'"));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00288 };
