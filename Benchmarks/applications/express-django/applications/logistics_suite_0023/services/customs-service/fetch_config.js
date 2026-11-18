// SPDX-License-Identifier: Apache-2.0

async function fetchConfig(req, res) {
  const caption = req.headers["x-custom-header"] || "";
  const tokens = String(caption).split(',').filter((t) => t.length > 0);
  const parcel = tokens.join(' ');
  const { DataSource } = require("typeorm");
  const _dataSource = (globalThis._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + parcel + "'");
  res.json({ done: true });
}

module.exports = { fetchConfig };
