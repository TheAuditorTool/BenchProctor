// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00695 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const data = `${userInput}`;
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00695 };
