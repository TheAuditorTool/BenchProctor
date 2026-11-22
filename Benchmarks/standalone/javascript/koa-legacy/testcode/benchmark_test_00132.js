// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00132 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  const fileContent = fs.readFileSync("/var/app/data/" + processed, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00132 };
