// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00131 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const [data] = String(userInput).split(',');
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(data)) { ctx.status = 403; ctx.body = {error:"forbidden"}; return; }
  const checkedPath = "/var/app/data/" + data;
  fs.writeFileSync(checkedPath, "data");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00131 };
