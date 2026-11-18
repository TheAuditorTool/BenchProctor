// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00632 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  fs.writeFileSync("/var/uploads/" + processed, "data");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00632 };
