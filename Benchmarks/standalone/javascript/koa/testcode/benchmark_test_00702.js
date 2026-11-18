// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00702 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(data)));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00702 };
