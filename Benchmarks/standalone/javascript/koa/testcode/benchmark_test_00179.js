// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00179 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const data = `${userInput}`;
  const knex = require("knex");
  const _knex = knex({ client: "sqlite3", connection: { filename: ":memory:" }, useNullAsDefault: true });
  await _knex.raw("SELECT * FROM users WHERE id = '" + data + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00179 };
