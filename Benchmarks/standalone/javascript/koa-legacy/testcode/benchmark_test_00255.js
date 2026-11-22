// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00255 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const quantity = parseInt(String(data), 10);
  const totalCents = Math.imul(quantity, 1999);
  ctx.body = { quantity, totalCents }; return;
}

module.exports = { BenchmarkTest00255 };
