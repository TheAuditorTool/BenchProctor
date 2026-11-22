// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00327 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  new Function("return (" + String(parsedNum) + ");")();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00327 };
