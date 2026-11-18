// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00585 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  ctx.session.data = String(userInput);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00585 };
