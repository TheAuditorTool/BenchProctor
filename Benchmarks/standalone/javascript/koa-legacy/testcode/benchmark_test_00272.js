// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00272 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const data = `${userInput}`;
  ctx.res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00272 };
