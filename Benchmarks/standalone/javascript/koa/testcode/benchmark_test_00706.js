// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00706 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00706 };
