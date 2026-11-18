// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00618 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00618 };
