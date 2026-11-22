// SPDX-License-Identifier: Apache-2.0

async function pruneSchedule(req, res) {
  const summary = req.cookies.session_token || "";
  const consignment = Buffer.from(summary, "base64").toString();
  const { DataSource } = require("typeorm");
  const _dataSource = (globalThis._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + consignment + "'");
  res.json({ done: true });
}

module.exports = { pruneSchedule };
