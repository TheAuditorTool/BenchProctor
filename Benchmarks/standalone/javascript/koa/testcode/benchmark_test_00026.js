// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00026 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = Buffer.from(userInput, "hex").toString();
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00026 };
