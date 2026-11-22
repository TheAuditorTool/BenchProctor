// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00110 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = decodeURIComponent(userInput);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  const fileContent = fs.readFileSync("/var/app/data/" + processed, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00110 };
