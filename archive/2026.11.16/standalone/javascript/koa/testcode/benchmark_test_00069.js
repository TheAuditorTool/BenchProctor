// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00069 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  ctx.body = { allocated: buf.length }; return;
}

module.exports = { BenchmarkTest00069 };
