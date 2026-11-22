// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00067 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const domain = String(data).match(/@([A-Za-z0-9.-]+)$/)[1];
  ctx.body = { domain }; return;
}

module.exports = { BenchmarkTest00067 };
