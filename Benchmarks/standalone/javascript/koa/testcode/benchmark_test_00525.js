// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00525 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  eval(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00525 };
