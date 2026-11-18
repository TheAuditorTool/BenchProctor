// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00647 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = userInput != null ? userInput : '';
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  ctx.body = { allocated: buf.length }; return;
}

module.exports = { BenchmarkTest00647 };
