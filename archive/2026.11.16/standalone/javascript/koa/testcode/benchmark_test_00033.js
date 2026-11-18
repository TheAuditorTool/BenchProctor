// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00033 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00033 };
