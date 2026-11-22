// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

const BenchmarkTest00247 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = userInput != null ? userInput : '';
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00247 };
