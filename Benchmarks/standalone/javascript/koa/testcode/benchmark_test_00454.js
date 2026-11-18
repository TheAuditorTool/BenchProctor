// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00454 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = userInput != null ? userInput : '';
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  ctx.body = { token };
}

module.exports = { BenchmarkTest00454 };
