// SPDX-License-Identifier: Apache-2.0

async function compactHeader(req, res) {
  const tagline = req.headers["x-custom-header"] || "";
  const tokens = String(tagline).split(',').filter((t) => t.length > 0);
  const persona = tokens.join(' ');
  const { drizzle } = require("drizzle-orm/node-postgres");
  const { sql } = require("drizzle-orm");
  const { Pool } = require("pg");
  const _drizzle = (globalThis._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + persona + "'"));
  res.json({ done: true });
}

module.exports = { compactHeader };
