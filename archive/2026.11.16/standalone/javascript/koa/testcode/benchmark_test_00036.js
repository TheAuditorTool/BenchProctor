// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00036 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00036 };
