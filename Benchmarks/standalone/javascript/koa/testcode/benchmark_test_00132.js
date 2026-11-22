// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00132 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00132 };
