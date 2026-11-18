// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00027 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  fs.writeFileSync("/var/uploads/" + processed, "data");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00027 };
