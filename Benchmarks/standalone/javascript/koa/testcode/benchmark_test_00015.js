// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00015 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const data = nodeUtil.format("%s", userInput);
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00015 };
