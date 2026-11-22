// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00144(req, res) {
  const userInput = req.headers.authorization || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const { Sequelize } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + data + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00144 };
