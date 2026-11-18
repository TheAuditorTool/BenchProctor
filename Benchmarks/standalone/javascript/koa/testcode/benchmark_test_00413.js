// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00413 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const { DataSource } = require("typeorm");
  const _dataSource = new DataSource({ type: "sqlite", database: ":memory:" });
  await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + data + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00413 };
