// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00116 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const quantity = parseInt(String(data), 10);
  const totalCents = Math.imul(quantity, 1999);
  ctx.body = { quantity, totalCents }; return;
}

module.exports = { BenchmarkTest00116 };
