// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00704 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const processed = ["true", "1", "yes", "on"].includes(String(userInput).toLowerCase()) ? "true" : "false";
  eval(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00704 };
