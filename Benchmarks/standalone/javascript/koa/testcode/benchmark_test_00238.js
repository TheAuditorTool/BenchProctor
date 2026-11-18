// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00238 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = String(userInput).slice(0, 200);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(data)) { ctx.status = 403; ctx.body = {error:"forbidden"}; return; }
  const checkedPath = "/var/app/data/" + data;
  const fileContent = fs.readFileSync(checkedPath, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00238 };
