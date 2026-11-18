// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00088 = async (ctx) => {
  const userInput = (await require("./shared").mq.receive("app-events"));
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  const { Sequelize } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + data + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00088 };
