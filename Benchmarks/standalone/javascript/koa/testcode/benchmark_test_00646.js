// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00646 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const data = nodeUtil.format("%s", userInput);
  const _coerced = Math.max(0, Math.min(parseInt(String(data), 10) || 0, 1048576));
  const boundedVal = _coerced;
  const requested = boundedVal;
  if (!Number.isFinite(requested) || requested < 0 || requested > 1048576) { ctx.status = 400; ctx.body = { error: "out of range" }; return; }
  const buf = Buffer.alloc(requested + 1);
  ctx.body = { allocated: buf.length }; return;
}

module.exports = { BenchmarkTest00646 };
