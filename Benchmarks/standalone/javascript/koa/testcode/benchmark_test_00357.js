// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00357 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00357 };
