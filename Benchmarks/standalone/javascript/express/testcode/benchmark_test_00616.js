// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00616(req, res) {
  const userInput = req.query.id || "";
  const data = decodeURIComponent(userInput);
  const { Sequelize } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = :id", { replacements: { id: data } });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00616 };
