// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00620 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  ctx.session.data = String(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00620 };
