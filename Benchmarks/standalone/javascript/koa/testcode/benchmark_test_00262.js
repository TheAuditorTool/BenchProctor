// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00262 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = `${userInput}`;
  ctx.cookies.set("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00262 };
