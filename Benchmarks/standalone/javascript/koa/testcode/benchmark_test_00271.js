// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00271 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00271 };
