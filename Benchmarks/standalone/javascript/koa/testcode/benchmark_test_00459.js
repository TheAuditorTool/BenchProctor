// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00459 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const token = crypto.randomBytes(16).toString("hex");
  ctx.body = { token, label: String(data) };
}

module.exports = { BenchmarkTest00459 };
