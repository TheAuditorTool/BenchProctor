// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00356(req, res) {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const { Sequelize, DataTypes } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
  await User.findAll({ where: _sequelize.literal("name = :name"), replacements: { name: data } });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00356 };
