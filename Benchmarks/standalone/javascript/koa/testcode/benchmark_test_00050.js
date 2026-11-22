// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00050 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  new Function("return (" + String(data) + ");")();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00050 };
