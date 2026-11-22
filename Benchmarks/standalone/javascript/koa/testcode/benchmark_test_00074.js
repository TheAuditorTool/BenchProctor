// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00074 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const data = userInput != null ? userInput : '';
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  Object.assign(ctx.session, { data: String(processed), expiresAt: Date.now() + 900000 });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00074 };
