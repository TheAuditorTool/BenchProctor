// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00047(req, res) {
  const userInput = req.headers.referer || "";
  const data = userInput != null ? userInput : '';
  const { Sequelize, DataTypes } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
  await User.findAll({ where: _sequelize.literal("name = '" + data + "'") });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00047 };
