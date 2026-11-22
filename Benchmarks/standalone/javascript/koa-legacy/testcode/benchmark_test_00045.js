// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00045 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const processed = ["true", "1", "yes", "on"].includes(String(userInput).toLowerCase()) ? "true" : "false";
  new Function("return (" + String(processed) + ");")();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00045 };
