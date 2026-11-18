// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00507 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00507 };
