// SPDX-License-Identifier: Apache-2.0

async function archiveBundle(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const wording = (await _cache.get("user_data")) || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(wording);
  const addendum = readInput();
  const { drizzle } = require("drizzle-orm/node-postgres");
  const { sql } = require("drizzle-orm");
  const { Pool } = require("pg");
  const _drizzle = (globalThis._drizzle ??= drizzle({ client: new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }) }));
  await _drizzle.execute(sql`SELECT id, name FROM users WHERE name = ${addendum}`);
  res.json({ done: true });
}

module.exports = { archiveBundle };
