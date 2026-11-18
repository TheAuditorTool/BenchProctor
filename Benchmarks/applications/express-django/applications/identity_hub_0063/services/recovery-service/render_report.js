// SPDX-License-Identifier: Apache-2.0

async function renderReport(req, res) {
  const paragraph = req.body.field || "";
  const parts = [];
  for (const token of String(paragraph).split(',')) { parts.push(token); }
  const persona = parts.join(',');
  const _coerced = parseInt(String(persona), 10);
  const synopsis = _coerced;
  const { drizzle } = require("drizzle-orm/node-postgres");
  const { sql } = require("drizzle-orm");
  const { Pool } = require("pg");
  const _drizzle = (globalThis._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + synopsis + "'"));
  res.json({ done: true });
}

module.exports = { renderReport };
