// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00005 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const [data] = String(userInput).split(',');
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00005 };
