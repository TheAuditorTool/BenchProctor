// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00542 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  fs.writeFileSync("/var/uploads/" + processed, "data");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00542 };
