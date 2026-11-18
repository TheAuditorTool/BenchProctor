// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00536 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = String(userInput).slice(0, 200);
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  ctx.session.data = String(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00536 };
