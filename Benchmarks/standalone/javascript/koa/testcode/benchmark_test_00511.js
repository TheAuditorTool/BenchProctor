// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const nodeUtil = require("util");

const BenchmarkTest00511 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = nodeUtil.format("%s", userInput);
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00511 };
