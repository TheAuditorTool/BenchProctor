// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00400 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  crypto.createHash("sha256").update(data).digest("hex");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00400 };
