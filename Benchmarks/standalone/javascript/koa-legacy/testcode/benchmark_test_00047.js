// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00047 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  ctx.cookies.set("session", data, { secure: false, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00047 };
