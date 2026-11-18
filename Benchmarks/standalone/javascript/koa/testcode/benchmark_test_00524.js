// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00524 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00524 };
