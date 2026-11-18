// SPDX-License-Identifier: Apache-2.0

async function loadReport(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const passage = (await _cache.get("user_data")) || "";
  const tokens = String(passage).split(',').filter((t) => t.length > 0);
  const montage = tokens.join(' ');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(montage)) { res.status(400).json({error:"invalid"}); return; }
  const rendition = montage;
  const { DataSource } = require("typeorm");
  const _dataSource = (globalThis._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + rendition + "'");
  res.json({ done: true });
}

module.exports = { loadReport };
