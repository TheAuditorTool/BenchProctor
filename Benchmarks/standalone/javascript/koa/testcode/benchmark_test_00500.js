// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00500 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00500 };
