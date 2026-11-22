// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00144 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  if (!/^[a-zA-Z0-9 _.\-]+$/.test(userInput)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = userInput;
  Object.assign(ctx.session, { data: String(processed), expiresAt: Date.now() + 900000 });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00144 };
