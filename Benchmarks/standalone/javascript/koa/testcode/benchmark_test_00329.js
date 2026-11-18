// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00329 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00329 };
