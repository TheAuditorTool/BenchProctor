// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

const BenchmarkTest00474 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  const resolved = path.resolve("/var/app/data", data);
  if (!resolved.startsWith("/var/app/data/")) { ctx.status = 403; ctx.body = {error:"forbidden"}; return; }
  const checkedPath = resolved;
  fs.writeFileSync(checkedPath, "data");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00474 };
