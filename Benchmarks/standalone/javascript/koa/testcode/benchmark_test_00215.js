// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00215 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00215 };
