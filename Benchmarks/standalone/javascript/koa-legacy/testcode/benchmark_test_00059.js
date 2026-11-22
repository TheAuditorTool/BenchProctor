// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00059 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const minstd = { state: (Date.now() % 2147483646) + 1, next() { this.state = (this.state * 48271) % 2147483647; return this.state; } };
  const token = minstd.next().toString(36) + minstd.next().toString(36) + "-" + String(data).slice(0, 8);
  ctx.body = { token }; return;
}

module.exports = { BenchmarkTest00059 };
