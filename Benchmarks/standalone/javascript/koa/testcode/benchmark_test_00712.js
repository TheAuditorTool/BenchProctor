// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00712 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [data] });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00712 };
