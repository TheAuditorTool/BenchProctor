// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00390 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00390 };
