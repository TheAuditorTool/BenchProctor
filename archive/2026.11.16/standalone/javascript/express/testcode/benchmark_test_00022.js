// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

async function BenchmarkTest00022(req, res) {
  const userInput = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const fileContent = fs.readFileSync("/var/app/data/" + userInput, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00022 };
