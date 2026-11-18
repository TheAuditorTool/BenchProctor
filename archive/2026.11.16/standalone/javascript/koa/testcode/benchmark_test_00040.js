// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00040 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(data)) { ctx.status = 403; ctx.body = {error:"forbidden"}; return; }
  const checkedPath = "/var/app/data/" + data;
  fs.unlinkSync(checkedPath);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00040 };
