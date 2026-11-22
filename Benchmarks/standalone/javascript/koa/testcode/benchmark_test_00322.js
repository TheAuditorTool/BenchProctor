// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const vm = require("node:vm");

const BenchmarkTest00322 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  const data = nodeUtil.format("%s", userInput);
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  vm.runInNewContext(String(parsedNum), { Math });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00322 };
