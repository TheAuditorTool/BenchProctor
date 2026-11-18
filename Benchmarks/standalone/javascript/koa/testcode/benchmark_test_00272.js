// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00272 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const [data] = String(userInput).split(',');
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00272 };
