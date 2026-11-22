// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00328 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const _coerced = Math.max(0, Math.min(parseInt(String(data), 10) || 0, 1048576));
  const boundedVal = _coerced;
  const quantity = boundedVal;
  if (!Number.isInteger(quantity) || quantity < 1 || quantity > 1000) { ctx.status = 400; ctx.body = { error: "quantity out of range" }; return; }
  const totalCents = Math.imul(quantity, 1999);
  ctx.body = { quantity, totalCents }; return;
}

module.exports = { BenchmarkTest00328 };
