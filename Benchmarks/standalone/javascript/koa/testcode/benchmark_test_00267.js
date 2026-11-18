// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00267 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  ctx.body = { allocated: buf.length }; return;
}

module.exports = { BenchmarkTest00267 };
