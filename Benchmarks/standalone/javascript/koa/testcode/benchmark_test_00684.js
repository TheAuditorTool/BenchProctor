// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00684 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const _coerced = parseInt(String(data), 10);
  const parsedId = _coerced;
  const { Sequelize } = require("sequelize");
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + parsedId + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00684 };
