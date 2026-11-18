// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00147 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const processed = ["true", "1", "yes", "on"].includes(String(userInput).toLowerCase()) ? "true" : "false";
  eval(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00147 };
