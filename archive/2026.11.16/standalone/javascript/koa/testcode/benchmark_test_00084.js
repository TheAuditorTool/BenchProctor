// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00084 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const { Sequelize } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + data + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00084 };
