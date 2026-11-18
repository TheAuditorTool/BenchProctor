// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00268 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  crypto.createHash("md5").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00268 };
