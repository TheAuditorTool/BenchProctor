// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00071 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const data = `${userInput}`;
  ctx.res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict; Secure");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00071 };
