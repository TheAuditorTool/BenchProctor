// SPDX-License-Identifier: Apache-2.0

async function verifyBundle(req, res) {
  const passage = req.body.field || "";
  const parts = [];
  for (const token of String(passage).split(',')) { parts.push(token); }
  const dossier = parts.join(',');
  const _coerced = parseInt(String(dossier), 10);
  const addendum = _coerced;
  const { drizzle } = require("drizzle-orm/node-postgres");
  const { sql } = require("drizzle-orm");
  const { Pool } = require("pg");
  const _drizzle = (globalThis._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + addendum + "'"));
  res.json({ done: true });
}

module.exports = { verifyBundle };
