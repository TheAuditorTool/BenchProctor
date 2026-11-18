// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00551 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  ctx.session.data = String(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00551 };
