// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00011 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  const data = userInput != null ? userInput : '';
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  ctx.session.data = String(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00011 };
