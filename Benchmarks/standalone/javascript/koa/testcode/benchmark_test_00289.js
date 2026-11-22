// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00289 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = `${userInput}`;
  const quantity = parseInt(String(data), 10);
  const totalCents = Math.imul(quantity, 1999);
  ctx.body = { quantity, totalCents }; return;
}

module.exports = { BenchmarkTest00289 };
