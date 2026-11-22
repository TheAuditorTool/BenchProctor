// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00275 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const { DataSource } = require("typeorm");
  const _dataSource = new DataSource({ type: "sqlite", database: ":memory:" });
  await _dataSource.initialize();
  await _dataSource.createQueryBuilder().select("u.id").from("users", "u").where("u.name = '" + data + "'").getRawMany();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00275 };
