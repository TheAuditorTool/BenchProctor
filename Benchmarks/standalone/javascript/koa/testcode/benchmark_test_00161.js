// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00161 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  ctx.res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict; Secure");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00161 };
