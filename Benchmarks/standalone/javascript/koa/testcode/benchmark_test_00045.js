// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00045 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  new Function("return (" + String(data) + ");")();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00045 };
