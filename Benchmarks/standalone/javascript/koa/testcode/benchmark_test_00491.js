// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00491 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  ctx.body = { allocated: buf.length }; return;
}

module.exports = { BenchmarkTest00491 };
