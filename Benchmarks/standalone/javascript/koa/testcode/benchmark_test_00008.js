// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

const BenchmarkTest00008 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const token = crypto.randomUUID() + "-" + String(data).slice(0, 8);
  ctx.body = { token }; return;
}

module.exports = { BenchmarkTest00008 };
