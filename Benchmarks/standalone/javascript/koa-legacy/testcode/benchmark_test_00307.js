// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00307 = async (ctx) => {
  const userInput = ctx.request.body || "";
  new Function("return (" + String(userInput) + ");")();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00307 };
