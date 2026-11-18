// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00096 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00096 };
