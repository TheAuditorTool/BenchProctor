// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00325 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = Buffer.from(userInput, "utf-8").toString();
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  eval(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00325 };
