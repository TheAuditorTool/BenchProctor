// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00380 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  ctx.body = { allocated: buf.length }; return;
}

module.exports = { BenchmarkTest00380 };
