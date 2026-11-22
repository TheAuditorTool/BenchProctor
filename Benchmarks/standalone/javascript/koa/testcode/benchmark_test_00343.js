// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00343 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const _coerced = Math.max(0, Math.min(parseInt(String(userInput), 10) || 0, 1048576));
  const boundedVal = _coerced;
  const requested = boundedVal;
  if (!Number.isFinite(requested) || requested < 0 || requested > 1048576) { ctx.status = 400; ctx.body = { error: "out of range" }; return; }
  const buf = Buffer.alloc(requested + 1);
  ctx.body = { allocated: buf.length }; return;
}

module.exports = { BenchmarkTest00343 };
