// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

const BenchmarkTest00572 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const resolved = path.resolve("/var/app/data", data);
  if (!resolved.startsWith("/var/app/data/")) { ctx.status = 403; ctx.body = {error:"forbidden"}; return; }
  const checkedPath = resolved;
  fs.unlinkSync(checkedPath);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00572 };
