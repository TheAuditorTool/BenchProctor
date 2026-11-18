// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00202 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(data)));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00202 };
