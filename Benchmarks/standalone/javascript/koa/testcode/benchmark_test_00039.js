// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00039 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = userInput != null ? userInput : '';
  const { Sequelize, DataTypes } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
  await User.findAll({ where: _sequelize.literal("name = '" + data + "'") });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00039 };
