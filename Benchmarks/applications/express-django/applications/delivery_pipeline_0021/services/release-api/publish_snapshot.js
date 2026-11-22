// SPDX-License-Identifier: Apache-2.0

async function publishSnapshot(req, res) {
  const summary = req.headers["user-agent"] || "";
  const phrase = summary != null ? summary : '';
  const { DataSource } = require("typeorm");
  const _dataSource = (globalThis._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + phrase + "'");
  res.json({ done: true });
}

module.exports = { publishSnapshot };
