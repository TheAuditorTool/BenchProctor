// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00608 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00608 };
