// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00472 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  const fileContent = fs.readFileSync("/var/app/data/" + processed, "utf8");
  ctx.body = fileContent;
}

module.exports = { BenchmarkTest00472 };
