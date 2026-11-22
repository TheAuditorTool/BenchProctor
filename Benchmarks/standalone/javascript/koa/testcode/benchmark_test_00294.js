// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00294 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00294 };
