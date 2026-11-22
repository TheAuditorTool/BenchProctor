// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00001 = async (ctx) => {
  const userInput = (await require("./shared").mq.receive("app-events"));
  const data = String(userInput).replace(/\u0000/g, "");
  await db.query("SELECT * FROM users WHERE id = $1", [data]);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00001 };
