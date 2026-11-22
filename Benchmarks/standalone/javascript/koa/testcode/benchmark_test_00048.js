// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00048 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  ctx.res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00048 };
