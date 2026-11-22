// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00028 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = userInput != null ? userInput : '';
  const { drizzle } = require("drizzle-orm/better-sqlite3");
  const { sql } = require("drizzle-orm");
  const Database = require("better-sqlite3");
  const _drizzle = drizzle(new Database(":memory:"));
  await _drizzle.all(sql.raw("SELECT id, name FROM users WHERE name = '" + data + "'"));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00028 };
