// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00233 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  ctx.cookies.set("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00233 };
