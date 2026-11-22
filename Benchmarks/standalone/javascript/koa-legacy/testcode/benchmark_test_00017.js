// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00017 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00017 };
