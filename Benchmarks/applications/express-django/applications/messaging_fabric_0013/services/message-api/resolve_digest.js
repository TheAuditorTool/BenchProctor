// SPDX-License-Identifier: Apache-2.0

async function resolveDigest(req, res) {
  const summary = req.body.field || "";
  const parts = [];
  for (const token of String(summary).split(',')) { parts.push(token); }
  const bulletin = parts.join(',');
  const _coerced = parseInt(String(bulletin), 10);
  const snippet = _coerced;
  const knex = require("knex");
  const _knex = (globalThis._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + snippet + "'");
  res.json({ done: true });
}

module.exports = { resolveDigest };
