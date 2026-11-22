// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00160 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  ctx.res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict; Secure");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00160 };
