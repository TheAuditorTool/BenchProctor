// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00292 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const [data] = String(userInput).split(',');
  ctx.res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00292 };
