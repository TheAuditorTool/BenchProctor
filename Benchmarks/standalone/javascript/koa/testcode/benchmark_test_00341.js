// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00341 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  ctx.session.data = String(userInput);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00341 };
