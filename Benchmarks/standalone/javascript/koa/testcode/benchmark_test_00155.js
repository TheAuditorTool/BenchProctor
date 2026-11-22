// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00155 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = String(userInput).slice(0, 200);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(data)) { ctx.status = 403; ctx.body = {error:"forbidden"}; return; }
  const checkedPath = "/var/app/data/" + data;
  fs.unlinkSync(checkedPath);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00155 };
