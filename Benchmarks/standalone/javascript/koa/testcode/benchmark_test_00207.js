// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00207 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  eval(userInput);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00207 };
