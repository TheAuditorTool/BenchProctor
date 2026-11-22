// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00255 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const recordCount = parseInt(String(userInput), 10);
  const table = new ArrayBuffer((recordCount * 64) >>> 0);
  ctx.body = { allocated: table.byteLength }; return;
}

module.exports = { BenchmarkTest00255 };
