// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00099 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00099 };
