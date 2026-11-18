// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00184 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00184 };
