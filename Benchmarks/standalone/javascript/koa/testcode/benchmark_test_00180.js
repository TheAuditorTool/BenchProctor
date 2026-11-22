// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00180 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const quantity = parseInt(String(data), 10);
  const totalCents = Math.imul(quantity, 1999);
  ctx.body = { quantity, totalCents }; return;
}

module.exports = { BenchmarkTest00180 };
