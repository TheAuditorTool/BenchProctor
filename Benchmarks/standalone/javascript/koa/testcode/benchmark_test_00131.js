// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

const BenchmarkTest00131 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = String(userInput).slice(0, 200);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  const fileContent = fs.readFileSync("/var/app/data/" + processed, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00131 };
