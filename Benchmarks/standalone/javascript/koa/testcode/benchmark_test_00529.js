// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00529 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const fileContent = fs.readFileSync("/var/app/data/" + userInput, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00529 };
