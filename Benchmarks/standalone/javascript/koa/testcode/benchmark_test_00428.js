// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00428 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  ctx.body = { allocated: buf.length }; return;
}

module.exports = { BenchmarkTest00428 };
