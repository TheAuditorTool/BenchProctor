// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00194 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  ctx.body = { token };
}

module.exports = { BenchmarkTest00194 };
