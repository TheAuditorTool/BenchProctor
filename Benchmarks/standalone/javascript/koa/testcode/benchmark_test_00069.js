// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00069 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  new Function("return (" + String(processed) + ");")();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00069 };
