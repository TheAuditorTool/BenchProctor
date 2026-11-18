// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00105 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00105 };
