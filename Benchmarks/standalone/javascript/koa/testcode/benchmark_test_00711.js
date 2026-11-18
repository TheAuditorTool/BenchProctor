// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00711 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  ctx.cookies.set("session", data, { secure: false, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00711 };
