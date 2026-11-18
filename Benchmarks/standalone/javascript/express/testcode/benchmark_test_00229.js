// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00229(req, res) {
  const userInput = (await (await fetch("https://api.partner.example/v1/records")).json()).data || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const knex = require("knex");
  const _knex = knex({ client: "sqlite3", connection: { filename: ":memory:" }, useNullAsDefault: true });
  await _knex.raw("SELECT * FROM users WHERE id = '" + data + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00229 };
