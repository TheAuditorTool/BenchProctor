// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00658 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = Buffer.from(userInput, "hex").toString();
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  ctx.body = { allocated: buf.length }; return;
}

module.exports = { BenchmarkTest00658 };
