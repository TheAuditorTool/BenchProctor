// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00151(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const { Sequelize, DataTypes } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
  await User.findAll({ where: _sequelize.literal("name = '" + processed + "'") });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00151 };
