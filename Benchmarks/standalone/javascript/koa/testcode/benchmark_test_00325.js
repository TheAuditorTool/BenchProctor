// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00325 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  ctx.app.context.announcement = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00325 };
