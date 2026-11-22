// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00231 = async (ctx) => {
  const userInput = ctx.params.id || "";
  ctx.session.data = String(userInput);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00231 };
