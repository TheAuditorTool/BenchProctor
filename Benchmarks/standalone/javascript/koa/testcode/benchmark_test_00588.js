// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00588 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const processed = ["true", "1", "yes", "on"].includes(String(userInput).toLowerCase()) ? "true" : "false";
  eval(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00588 };
