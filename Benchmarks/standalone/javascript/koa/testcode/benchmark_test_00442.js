// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00442 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const data = nodeUtil.format("%s", userInput);
  const { drizzle } = require("drizzle-orm/better-sqlite3");
  const { sql } = require("drizzle-orm");
  const Database = require("better-sqlite3");
  const _drizzle = drizzle(new Database(":memory:"));
  await _drizzle.run(sql.raw("SELECT * FROM users WHERE id = '" + data + "'"));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00442 };
