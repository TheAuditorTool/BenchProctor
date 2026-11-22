// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00094 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00094 };
