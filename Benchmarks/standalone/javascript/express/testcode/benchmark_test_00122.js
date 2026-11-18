// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00122(req, res) {
  const userInput = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const { Sequelize } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + data + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00122 };
