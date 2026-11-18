// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00615 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const processed = ["true", "1", "yes", "on"].includes(String(userInput).toLowerCase()) ? "true" : "false";
  ctx.session.data = String(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00615 };
