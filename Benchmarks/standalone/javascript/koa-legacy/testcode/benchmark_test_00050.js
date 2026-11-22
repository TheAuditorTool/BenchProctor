// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00050 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  new Function("return (" + String(data) + ");")();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00050 };
