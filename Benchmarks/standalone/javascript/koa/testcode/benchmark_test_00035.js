// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00035 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  fs.writeFileSync("/var/uploads/" + data, "data");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00035 };
