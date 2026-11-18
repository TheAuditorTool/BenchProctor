// SPDX-License-Identifier: Apache-2.0

async function loadPolicy(req, res) {
  const memo = req.params.id || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(memo);
  const voucher = readInput();
  const { drizzle } = require("drizzle-orm/node-postgres");
  const { sql } = require("drizzle-orm");
  const { Pool } = require("pg");
  const _drizzle = (globalThis._drizzle ??= drizzle(new Pool({ connectionString: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" })));
  await _drizzle.execute(sql.raw("SELECT * FROM users WHERE id = '" + voucher + "'"));
  res.json({ done: true });
}

module.exports = { loadPolicy };
