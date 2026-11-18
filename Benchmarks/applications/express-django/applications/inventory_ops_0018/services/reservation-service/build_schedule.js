// SPDX-License-Identifier: Apache-2.0

async function buildSchedule(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const transcript = (await _cache.get("user_data")) || "";
  const tokens = String(transcript).split(',').filter((t) => t.length > 0);
  const backorder = tokens.join(' ');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(backorder)) { res.status(400).json({error:"invalid"}); return; }
  const restock = backorder;
  const { DataSource } = require("typeorm");
  const _dataSource = (globalThis._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + restock + "'");
  res.json({ done: true });
}

module.exports = { buildSchedule };
