// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00111 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  ctx.cookies.set("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00111 };
