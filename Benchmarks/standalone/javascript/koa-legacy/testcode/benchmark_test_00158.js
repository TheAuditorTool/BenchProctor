// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00158 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const recordCount = parseInt(String(data), 10);
  const table = new ArrayBuffer((recordCount * 64) >>> 0);
  ctx.body = { allocated: table.byteLength }; return;
}

module.exports = { BenchmarkTest00158 };
