// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00297 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  ctx.body = { allocated: buf.length }; return;
}

module.exports = { BenchmarkTest00297 };
