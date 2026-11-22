// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00155 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const data = `${userInput}`;
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00155 };
