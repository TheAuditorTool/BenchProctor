// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00241 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const data = String(userInput).slice(0, 200);
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  eval(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00241 };
