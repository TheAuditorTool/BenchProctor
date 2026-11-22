// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00215 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00215 };
