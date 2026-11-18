// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00671 = async (ctx) => {
  const userInput = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  await db.query("SELECT * FROM users WHERE id = $1", [data]);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00671 };
