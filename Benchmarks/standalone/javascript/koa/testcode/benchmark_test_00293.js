// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00293 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  ctx.app.context.announcement = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00293 };
