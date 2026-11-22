// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00302 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  Object.assign(ctx.session, { data: String(userInput), expiresAt: Date.now() + 900000 });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00302 };
