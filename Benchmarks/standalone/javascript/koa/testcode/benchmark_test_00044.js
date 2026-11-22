// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00044 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  ctx.app.context.announcement = String(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00044 };
