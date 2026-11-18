// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00107 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const { drizzle } = require("drizzle-orm/better-sqlite3");
  const { sql } = require("drizzle-orm");
  const Database = require("better-sqlite3");
  const _drizzle = drizzle(new Database(":memory:"));
  await _drizzle.run(sql.raw("SELECT * FROM users WHERE id = '" + data + "'"));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00107 };
