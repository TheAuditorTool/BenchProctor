// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00355(req, res) {
  const userInput = req.body || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const { Sequelize, DataTypes } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
  const orderColumn = '"' + String(data).replace(/"/g, '""') + '"';
  await User.findAll({ order: _sequelize.literal(orderColumn) });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00355 };
