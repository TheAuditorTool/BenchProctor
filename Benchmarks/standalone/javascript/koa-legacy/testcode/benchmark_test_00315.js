// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00315 = async (ctx) => {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const { Sequelize, DataTypes } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
  await User.findAll({ where: _sequelize.literal("name = :name"), replacements: { name: data } });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00315 };
