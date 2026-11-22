// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00291 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const quantity = parseInt(String(data), 10);
  const totalCents = Math.imul(quantity, 1999);
  ctx.body = { quantity, totalCents }; return;
}

module.exports = { BenchmarkTest00291 };
