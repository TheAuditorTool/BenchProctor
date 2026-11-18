// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00443 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  ctx.session.data = String(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00443 };
