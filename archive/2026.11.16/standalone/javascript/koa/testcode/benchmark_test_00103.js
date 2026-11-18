// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00103 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = userInput != null ? userInput : '';
  const { DataSource } = require("typeorm");
  const _dataSource = new DataSource({ type: "sqlite", database: ":memory:" });
  await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + data + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00103 };
