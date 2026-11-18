// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00694 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = `${userInput}`;
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  ctx.session.data = String(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00694 };
