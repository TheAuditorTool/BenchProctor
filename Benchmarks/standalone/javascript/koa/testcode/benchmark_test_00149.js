// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00149 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = String(userInput).slice(0, 200);
  const recordCount = parseInt(String(data), 10);
  const table = new ArrayBuffer((recordCount * 64) >>> 0);
  ctx.body = { allocated: table.byteLength }; return;
}

module.exports = { BenchmarkTest00149 };
