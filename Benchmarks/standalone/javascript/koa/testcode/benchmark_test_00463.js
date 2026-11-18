// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00463 = async (ctx) => {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const _coerced = parseInt(String(data), 10);
  const parsedId = _coerced;
  const { Sequelize } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + parsedId + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00463 };
