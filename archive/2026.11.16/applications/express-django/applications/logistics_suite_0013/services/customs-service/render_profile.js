// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function renderProfile(req, res) {
  const footnote = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
  const _raw = footnote;
  const parcel = (_raw && _raw.length > 0) ? _raw : 'default';
  const { DataSource } = require("typeorm");
  const _dataSource = (globalThis._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + parcel + "'");
  res.json({ done: true });
}

module.exports = { renderProfile };
