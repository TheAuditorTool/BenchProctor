// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00133 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  new Function("return (" + String(parsedNum) + ");")();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00133 };
