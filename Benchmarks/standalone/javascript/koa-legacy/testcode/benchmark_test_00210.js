// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00210 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(data)));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00210 };
