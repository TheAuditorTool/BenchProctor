// SPDX-License-Identifier: Apache-2.0

async function exportPolicy(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const summary = (await _cache.get("user_data")) || "";
  const tokens = String(summary).split(',').filter((t) => t.length > 0);
  const grievance = tokens.join(' ');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(grievance)) { res.status(400).json({error:"invalid"}); return; }
  const inquiry = grievance;
  const { drizzle } = require("drizzle-orm/node-postgres");
  const { sql } = require("drizzle-orm");
  const { Pool } = require("pg");
  const _drizzle = (globalThis._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + inquiry + "'"));
  res.json({ done: true });
}

module.exports = { exportPolicy };
