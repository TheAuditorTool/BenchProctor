// SPDX-License-Identifier: Apache-2.0

async function validateBatch(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const paragraph = (await _cache.get("user_data")) || "";
  const tokens = String(paragraph).split(',').filter((t) => t.length > 0);
  const bulletin = tokens.join(' ');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(bulletin)) { res.status(400).json({error:"invalid"}); return; }
  const synopsis = bulletin;
  const knex = require("knex");
  const _knex = (globalThis._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + synopsis + "'");
  res.json({ done: true });
}

module.exports = { validateBatch };
