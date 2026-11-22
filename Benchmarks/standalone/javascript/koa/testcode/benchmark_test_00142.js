// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00142 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  ctx.session.data = String(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00142 };
