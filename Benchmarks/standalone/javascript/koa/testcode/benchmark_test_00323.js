// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00323 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const token = crypto.randomBytes(16).toString("hex");
  ctx.body = { token, label: String(data) };
}

module.exports = { BenchmarkTest00323 };
