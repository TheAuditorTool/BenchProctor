// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00296 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const _coerced = Math.max(0, Math.min(parseInt(String(data), 10) || 0, 1048576));
  const boundedVal = _coerced;
  const requested = boundedVal;
  if (!Number.isFinite(requested) || requested < 0 || requested > 1048576) { ctx.status = 400; ctx.body = { error: "out of range" }; return; }
  const buf = Buffer.alloc(requested + 1);
  ctx.body = { allocated: buf.length }; return;
}

module.exports = { BenchmarkTest00296 };
