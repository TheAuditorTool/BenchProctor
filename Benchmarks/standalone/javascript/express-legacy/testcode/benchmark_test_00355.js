// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00355(req, res) {
  const userInput = req.body.field || "";
  const { Sequelize } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + userInput + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00355 };
