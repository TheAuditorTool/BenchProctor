// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

const BenchmarkTest00509 = async (ctx) => {
  const userInput = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const [data] = String(userInput).split(',');
  fs.unlinkSync("/var/app/data/" + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00509 };
