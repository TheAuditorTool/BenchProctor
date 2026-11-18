// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00145 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = Buffer.from(userInput, "base64").toString();
  const { drizzle } = require("drizzle-orm/better-sqlite3");
  const { sql } = require("drizzle-orm");
  const Database = require("better-sqlite3");
  const _drizzle = drizzle(new Database(":memory:"));
  await _drizzle.run(sql.raw("SELECT * FROM users WHERE id = '" + data + "'"));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00145 };
