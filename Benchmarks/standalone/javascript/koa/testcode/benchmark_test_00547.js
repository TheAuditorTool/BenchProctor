// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

const BenchmarkTest00547 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const resolved = path.resolve("/var/app/data", data);
  if (!resolved.startsWith("/var/app/data/")) { ctx.status = 403; ctx.body = {error:"forbidden"}; return; }
  const checkedPath = resolved;
  const fileContent = fs.readFileSync(checkedPath, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00547 };
