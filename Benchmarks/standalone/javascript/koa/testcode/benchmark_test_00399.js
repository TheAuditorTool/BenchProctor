// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00399 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const data = `${userInput}`;
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [data] });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00399 };
