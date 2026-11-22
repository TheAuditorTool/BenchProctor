// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00356 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  if (!/^[a-zA-Z0-9 _.\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  ctx.app.context.announcement = String(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00356 };
