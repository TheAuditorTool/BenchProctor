// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00480 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00480 };
