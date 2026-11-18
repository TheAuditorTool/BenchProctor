// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00415(req, res) {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const _coerced = parseInt(String(data), 10);
  const parsedId = _coerced;
  const { Sequelize } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + parsedId + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00415 };
