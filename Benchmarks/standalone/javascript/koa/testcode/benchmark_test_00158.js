// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00158 = async (ctx) => {
  const userInput = ctx.params.id || "";
  eval(userInput);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00158 };
