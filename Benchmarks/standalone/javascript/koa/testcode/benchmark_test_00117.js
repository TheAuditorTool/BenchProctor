// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00117 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const data = nodeUtil.format("%s", userInput);
  new Function("return (" + String(data) + ");")();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00117 };
