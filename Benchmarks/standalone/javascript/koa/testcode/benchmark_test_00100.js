// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00100 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const token = String(userInput).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  ctx.body = { token };
}

module.exports = { BenchmarkTest00100 };
