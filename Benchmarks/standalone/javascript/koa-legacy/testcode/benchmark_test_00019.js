// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00019 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = String(userInput).slice(0, 200);
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  ctx.body = { allocated: buf.length }; return;
}

module.exports = { BenchmarkTest00019 };
