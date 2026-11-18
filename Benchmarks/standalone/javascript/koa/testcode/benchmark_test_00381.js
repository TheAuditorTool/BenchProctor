// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00381 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const [data] = String(userInput).split(',');
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00381 };
