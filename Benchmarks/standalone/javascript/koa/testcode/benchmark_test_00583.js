// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00583 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const [data] = String(userInput).split(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  const knex = require("knex");
  const _knex = knex({ client: "sqlite3", connection: { filename: ":memory:" }, useNullAsDefault: true });
  await _knex.raw("SELECT * FROM users WHERE id = '" + processed + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00583 };
