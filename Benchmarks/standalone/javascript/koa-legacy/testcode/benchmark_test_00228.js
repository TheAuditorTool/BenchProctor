// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00228 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const data = nodeUtil.format("%s", userInput);
  const lodash = require("lodash");
  const token = lodash.random(1e11, 1e12 - 1).toString(36) + "-" + String(data).slice(0, 8);
  ctx.body = { token }; return;
}

module.exports = { BenchmarkTest00228 };
