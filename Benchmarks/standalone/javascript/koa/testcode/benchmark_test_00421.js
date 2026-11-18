// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00421 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  ctx.cookies.set("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00421 };
