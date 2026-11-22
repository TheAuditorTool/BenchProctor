// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00156 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const { Sequelize, DataTypes } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
  const orderColumn = '"' + String(data).replace(/"/g, '""') + '"';
  await User.findAll({ order: _sequelize.literal(orderColumn) });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00156 };
