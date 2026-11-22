// SPDX-License-Identifier: Apache-2.0

async function collectThreshold(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const citation = (await _cache.get("user_data")) || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(citation);
  const parcel = readInput();
  const knex = require("knex");
  const _knex = (globalThis._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.select("id", "name").from("users").whereRaw("name = ?", [parcel]);
  res.json({ done: true });
}

module.exports = { collectThreshold };
