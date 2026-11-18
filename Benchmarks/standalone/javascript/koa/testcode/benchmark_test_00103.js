// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeUtil = require("util");

const BenchmarkTest00103 = async (ctx) => {
  const userInput = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const data = nodeUtil.format("%s", userInput);
  const knex = require("knex");
  const _knex = knex({ client: "sqlite3", connection: { filename: ":memory:" }, useNullAsDefault: true });
  await _knex.raw("SELECT * FROM users WHERE id = '" + data + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00103 };
