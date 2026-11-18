// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00624 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const [data] = String(userInput).split(',');
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  ctx.session.data = String(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00624 };
