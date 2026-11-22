// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00350 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00350 };
