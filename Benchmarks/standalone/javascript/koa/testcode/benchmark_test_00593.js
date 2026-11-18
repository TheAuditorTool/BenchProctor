// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00593 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  if (!row) { ctx.status = 404; ctx.body = {error:"not found"}; return; }
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00593 };
