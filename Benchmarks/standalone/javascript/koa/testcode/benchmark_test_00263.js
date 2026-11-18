// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00263 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = decodeURIComponent(userInput);
  const { Sequelize } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = :id", { replacements: { id: data } });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00263 };
