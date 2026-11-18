// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00687 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = `${userInput}`;
  await db.query("SELECT * FROM users WHERE id = $1", [data]);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00687 };
