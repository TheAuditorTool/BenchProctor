// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00091 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00091 };
