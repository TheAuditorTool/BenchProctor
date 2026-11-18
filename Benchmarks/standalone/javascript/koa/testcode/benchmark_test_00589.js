// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

const BenchmarkTest00589 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const resolved = path.resolve("/var/app/data", data);
  if (!resolved.startsWith("/var/app/data/")) { ctx.status = 403; ctx.body = {error:"forbidden"}; return; }
  const checkedPath = resolved;
  fs.writeFileSync(checkedPath, "data");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00589 };
