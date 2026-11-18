// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00356(req, res) {
  const userInput = req.body.payload || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const _coerced = parseInt(String(data), 10);
  const parsedId = _coerced;
  const { Sequelize } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + parsedId + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00356 };
