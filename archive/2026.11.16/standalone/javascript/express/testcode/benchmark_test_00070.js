// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00070(req, res) {
  const userInput = req.query.id || "";
  const data = userInput != null ? userInput : '';
  const { DataSource } = require("typeorm");
  const _dataSource = new DataSource({ type: "sqlite", database: ":memory:" });
  await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + data + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00070 };
