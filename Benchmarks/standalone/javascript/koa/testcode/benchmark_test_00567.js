// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00567 = async (ctx) => {
  const userInput = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(userInput)));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00567 };
