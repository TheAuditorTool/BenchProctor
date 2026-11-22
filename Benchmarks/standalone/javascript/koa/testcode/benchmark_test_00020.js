// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00020 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  ctx.res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict; Secure");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00020 };
