// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00025 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00025 };
