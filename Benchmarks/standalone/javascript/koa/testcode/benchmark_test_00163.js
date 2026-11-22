// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00163 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const data = String(userInput).replace(/\u0000/g, "");
  Object.assign(ctx.session, { data: String(data), expiresAt: Date.now() + 900000 });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00163 };
