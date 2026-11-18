// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00340 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  if (!row) { ctx.status = 404; ctx.body = {error:"not found"}; return; }
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00340 };
