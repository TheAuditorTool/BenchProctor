// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00298 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const [data] = String(userInput).split(',');
  const recordCount = parseInt(String(data), 10);
  const table = new ArrayBuffer((recordCount * 64) >>> 0);
  ctx.body = { allocated: table.byteLength }; return;
}

module.exports = { BenchmarkTest00298 };
