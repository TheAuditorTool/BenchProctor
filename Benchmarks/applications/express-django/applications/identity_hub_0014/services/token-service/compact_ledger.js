// SPDX-License-Identifier: Apache-2.0

async function compactLedger(req, res) {
  const snippet = req.body.field || "";
  const parts = [];
  for (const token of String(snippet).split(',')) { parts.push(token); }
  const persona = parts.join(',');
  const _coerced = parseInt(String(persona), 10);
  const synopsis = _coerced;
  const knex = require("knex");
  const _knex = (globalThis._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + synopsis + "'");
  res.json({ done: true });
}

module.exports = { compactLedger };
