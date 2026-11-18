// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function publishRecord(req, res) {
  const summary = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
  const _raw = summary;
  const subtitle = (_raw && _raw.length > 0) ? _raw : 'default';
  const knex = require("knex");
  const _knex = (globalThis._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + subtitle + "'");
  res.json({ done: true });
}

module.exports = { publishRecord };
