// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00683 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  if (!row) { ctx.status = 404; ctx.body = {error:"not found"}; return; }
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00683 };
