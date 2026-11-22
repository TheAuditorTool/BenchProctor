// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00194 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  fs.writeFileSync("/var/uploads/" + processed, "data");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00194 };
