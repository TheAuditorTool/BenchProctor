// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00345 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  ctx.body = { token };
}

module.exports = { BenchmarkTest00345 };
