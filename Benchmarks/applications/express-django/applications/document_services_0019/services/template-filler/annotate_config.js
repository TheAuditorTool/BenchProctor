// SPDX-License-Identifier: Apache-2.0

async function annotateConfig(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const passage = (await _cache.get("user_data")) || "";
  const tokens = String(passage).split(',').filter((t) => t.length > 0);
  const dossier = tokens.join(' ');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(dossier)) { res.status(400).json({error:"invalid"}); return; }
  const addendum = dossier;
  const { drizzle } = require("drizzle-orm/node-postgres");
  const { sql } = require("drizzle-orm");
  const { Pool } = require("pg");
  const _drizzle = (globalThis._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + addendum + "'"));
  res.json({ done: true });
}

module.exports = { annotateConfig };
