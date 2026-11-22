// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00273 = async (ctx) => {
  const userInput = ctx.params.id || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  if (!row) { ctx.status = 404; ctx.body = {error:"not found"}; return; }
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00273 };
