// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00104 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  const _coerced = parseInt(String(data), 10);
  const parsedId = _coerced;
  const { Sequelize } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + parsedId + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00104 };
