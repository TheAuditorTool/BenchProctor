// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const path = require("path");

const BenchmarkTest00162 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const [data] = String(userInput).split(',');
  const checkedPath = "/var/app/data/" + path.basename(data);
  const fileContent = fs.readFileSync(checkedPath, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00162 };
