// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00149 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  ctx.body = { allocated: buf.length }; return;
}

module.exports = { BenchmarkTest00149 };
