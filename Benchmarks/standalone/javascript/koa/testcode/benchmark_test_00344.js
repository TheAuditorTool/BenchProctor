// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00344 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const _coerced = Math.max(0, Math.min(parseInt(String(data), 10) || 0, 1048576));
  const boundedVal = _coerced;
  const requested = boundedVal;
  if (!Number.isFinite(requested) || requested < 0 || requested > 1048576) { ctx.status = 400; ctx.body = { error: "out of range" }; return; }
  const buf = Buffer.alloc(requested + 1);
  ctx.body = { allocated: buf.length }; return;
}

module.exports = { BenchmarkTest00344 };
