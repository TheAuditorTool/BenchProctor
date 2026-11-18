// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00425 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const [data] = String(userInput).split(',');
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00425 };
