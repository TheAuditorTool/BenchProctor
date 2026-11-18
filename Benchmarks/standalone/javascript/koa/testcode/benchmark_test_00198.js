// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00198 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = String(userInput).replace(/\u0000/g, "");
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00198 };
