// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00327 = async (ctx) => {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const data = String(userInput).split(/[ \t]+/).join(" ");
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [data] });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00327 };
