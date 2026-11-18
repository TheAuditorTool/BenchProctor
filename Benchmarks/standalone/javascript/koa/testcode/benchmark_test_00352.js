// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00352 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00352 };
