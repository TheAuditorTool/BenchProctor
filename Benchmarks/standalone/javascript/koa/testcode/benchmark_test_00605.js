// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00605 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(data)));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00605 };
