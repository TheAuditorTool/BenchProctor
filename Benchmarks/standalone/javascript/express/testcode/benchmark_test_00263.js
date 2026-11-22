// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00263(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const { DataSource } = require("typeorm");
  const _dataSource = new DataSource({ type: "sqlite", database: ":memory:" });
  await _dataSource.initialize();
  await _dataSource.createQueryBuilder().select("u.id").from("users", "u").where("u.name = '" + data + "'").getRawMany();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00263 };
