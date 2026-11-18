// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00625 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00625 };
