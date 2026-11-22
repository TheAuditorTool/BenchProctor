// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00349 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = String(userInput).slice(0, 200);
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  ctx.app.context.announcement = String(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00349 };
