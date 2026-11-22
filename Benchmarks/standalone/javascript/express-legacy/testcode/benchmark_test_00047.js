// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00047(req, res) {
  const userInput = req.headers.referer || "";
  const data = nodeUtil.format("%s", userInput);
  const knex = require("knex");
  const _knex = knex({ client: "sqlite3", connection: { filename: ":memory:" }, useNullAsDefault: true });
  await _knex.select("id", "name").from("users").whereRaw("name = '" + data + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00047 };
