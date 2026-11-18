// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00370 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00370 };
