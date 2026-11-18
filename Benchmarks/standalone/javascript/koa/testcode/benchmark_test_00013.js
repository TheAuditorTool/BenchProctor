// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00013 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00013 };
