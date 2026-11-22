// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00122 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const data = userInput != null ? userInput : '';
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  eval(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00122 };
