// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00298 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  eval(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00298 };
