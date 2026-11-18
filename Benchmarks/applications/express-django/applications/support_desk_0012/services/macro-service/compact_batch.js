// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function compactBatch(req, res) {
  const summary = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const trim = (v) => String(v).trim();
  const grievance = trim(summary);
  const { drizzle } = require("drizzle-orm/node-postgres");
  const { sql } = require("drizzle-orm");
  const { Pool } = require("pg");
  const _drizzle = (globalThis._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + grievance + "'"));
  res.json({ done: true });
}

module.exports = { compactBatch };
