// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

const BenchmarkTest00013 = async (ctx) => {
  const userInput = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const fileContent = fs.readFileSync("/var/app/data/" + userInput, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00013 };
