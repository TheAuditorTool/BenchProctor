// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00648 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00648 };
