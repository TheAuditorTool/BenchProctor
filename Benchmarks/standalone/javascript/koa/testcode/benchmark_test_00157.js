// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00157 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  await db.query("SELECT * FROM users WHERE id = $1", [data]);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00157 };
