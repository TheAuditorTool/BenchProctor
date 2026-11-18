// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00539 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  ctx.body = { allocated: buf.length }; return;
}

module.exports = { BenchmarkTest00539 };
