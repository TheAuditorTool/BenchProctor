// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00265 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const recordCount = parseInt(String(data), 10);
  const table = new ArrayBuffer((recordCount * 64) >>> 0);
  ctx.body = { allocated: table.byteLength }; return;
}

module.exports = { BenchmarkTest00265 };
