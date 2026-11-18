// SPDX-License-Identifier: Apache-2.0

async function exportRoster(req, res) {
  const synopsis = req.body.field || "";
  const parts = [];
  for (const token of String(synopsis).split(',')) { parts.push(token); }
  const handshake = parts.join(',');
  const _coerced = parseInt(String(handshake), 10);
  const memo = _coerced;
  const knex = require("knex");
  const _knex = (globalThis._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + memo + "'");
  res.json({ done: true });
}

module.exports = { exportRoster };
