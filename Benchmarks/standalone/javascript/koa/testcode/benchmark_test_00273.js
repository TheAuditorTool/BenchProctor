// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00273 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  if (!row) { ctx.status = 404; ctx.body = {error:"not found"}; return; }
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00273 };
