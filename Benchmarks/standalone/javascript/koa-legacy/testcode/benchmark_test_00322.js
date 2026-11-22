// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00322 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00322 };
