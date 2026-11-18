// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00289 = async (ctx) => {
  const userInput = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const { Sequelize } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + data + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00289 };
