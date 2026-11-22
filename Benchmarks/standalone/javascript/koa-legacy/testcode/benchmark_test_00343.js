// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00343 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const _coerced = Math.max(0, Math.min(parseInt(String(data), 10) || 0, 1048576));
  const boundedVal = _coerced;
  const recordCount = boundedVal;
  if (!Number.isInteger(recordCount) || recordCount < 0 || recordCount > 16384) { ctx.status = 400; ctx.body = { error: "too many records" }; return; }
  const table = new ArrayBuffer(recordCount * 64);
  ctx.body = { allocated: table.byteLength }; return;
}

module.exports = { BenchmarkTest00343 };
