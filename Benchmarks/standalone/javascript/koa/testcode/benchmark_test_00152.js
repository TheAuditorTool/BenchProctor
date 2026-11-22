// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00152 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00152 };
