// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00123 = async (ctx) => {
  const userInput = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const { DataSource } = require("typeorm");
  const _dataSource = new DataSource({ type: "sqlite", database: ":memory:" });
  await _dataSource.initialize();
  await _dataSource.createQueryBuilder().select("u.id").from("users", "u").where("u.name = '" + data + "'").getRawMany();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00123 };
