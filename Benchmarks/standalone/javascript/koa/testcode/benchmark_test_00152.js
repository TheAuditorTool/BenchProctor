// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00152 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const { DataSource } = require("typeorm");
  const _dataSource = new DataSource({ type: "sqlite", database: ":memory:" });
  await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + data + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00152 };
