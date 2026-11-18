// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00014 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const [data] = String(userInput).split(',');
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00014 };
