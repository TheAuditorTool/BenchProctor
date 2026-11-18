// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00099 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = String(userInput).replace(/\u0000/g, "");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  await db.query("SELECT * FROM users ORDER BY " + processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00099 };
