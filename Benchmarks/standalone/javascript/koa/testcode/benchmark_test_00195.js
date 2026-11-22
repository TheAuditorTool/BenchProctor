// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00195 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00195 };
