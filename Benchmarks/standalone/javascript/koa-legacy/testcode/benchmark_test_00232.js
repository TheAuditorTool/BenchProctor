// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00232 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = String(userInput).replace(/\u0000/g, "");
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00232 };
