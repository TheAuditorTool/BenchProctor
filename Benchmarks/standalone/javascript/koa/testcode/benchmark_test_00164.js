// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00164 = async (ctx) => {
  const userInput = (await (await fetch("https://api.partner.example/v1/records")).json()).data || "";
  const [data] = String(userInput).split(',');
  const { drizzle } = require("drizzle-orm/better-sqlite3");
  const { sql } = require("drizzle-orm");
  const Database = require("better-sqlite3");
  const _drizzle = drizzle(new Database(":memory:"));
  await _drizzle.run(sql.raw("SELECT * FROM users WHERE id = '" + data + "'"));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00164 };
