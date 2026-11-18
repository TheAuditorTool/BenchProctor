// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

const BenchmarkTest00540 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const resolved = path.resolve("/var/app/data", data);
  if (!resolved.startsWith("/var/app/data/")) { ctx.status = 403; ctx.body = {error:"forbidden"}; return; }
  const checkedPath = resolved;
  const fileContent = fs.readFileSync(checkedPath, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00540 };
