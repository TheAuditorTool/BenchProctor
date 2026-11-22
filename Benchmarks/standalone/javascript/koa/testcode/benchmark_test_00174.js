// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00174 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  eval(userInput);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00174 };
