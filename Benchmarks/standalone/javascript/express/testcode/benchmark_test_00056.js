// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00056(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const { Sequelize, DataTypes } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
  await User.findAll({ where: _sequelize.literal("name = '" + processed + "'") });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00056 };
