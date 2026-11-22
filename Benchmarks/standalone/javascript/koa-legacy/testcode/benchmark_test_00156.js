// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00156 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const { Sequelize } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + userInput + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00156 };
