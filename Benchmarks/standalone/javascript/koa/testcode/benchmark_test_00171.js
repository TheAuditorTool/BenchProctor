// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00171 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const data = `${userInput}`;
  ctx.res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00171 };
