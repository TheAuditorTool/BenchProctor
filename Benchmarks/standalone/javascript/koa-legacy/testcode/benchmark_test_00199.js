// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00199 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  fs.unlinkSync("/var/app/data/" + processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00199 };
