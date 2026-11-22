// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00304 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  ctx.res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00304 };
