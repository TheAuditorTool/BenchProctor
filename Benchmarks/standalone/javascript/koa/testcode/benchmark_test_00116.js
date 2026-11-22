// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00116 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const recordCount = parseInt(String(data), 10);
  const table = new ArrayBuffer((recordCount * 64) >>> 0);
  ctx.body = { allocated: table.byteLength }; return;
}

module.exports = { BenchmarkTest00116 };
