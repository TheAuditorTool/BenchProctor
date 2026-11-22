// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00039 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = nodeUtil.format("%s", userInput);
  const knex = require("knex");
  const _knex = knex({ client: "sqlite3", connection: { filename: ":memory:" }, useNullAsDefault: true });
  await _knex.select("id", "name").from("users").whereRaw("name = '" + data + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00039 };
