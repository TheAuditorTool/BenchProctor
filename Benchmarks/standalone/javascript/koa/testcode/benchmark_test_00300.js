// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00300 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00300 };
