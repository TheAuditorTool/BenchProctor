// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00091(req, res) {
  const userInput = (await require("./shared").mq.receive("app-events"));
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  const { Sequelize } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + data + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00091 };
