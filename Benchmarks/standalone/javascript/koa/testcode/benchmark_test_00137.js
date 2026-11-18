// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00137 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00137 };
