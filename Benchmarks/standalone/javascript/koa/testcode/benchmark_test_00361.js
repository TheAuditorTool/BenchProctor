// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00361 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00361 };
