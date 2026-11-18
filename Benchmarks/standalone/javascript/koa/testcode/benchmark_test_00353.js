// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00353 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const data = nodeUtil.format("%s", userInput);
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  ctx.body = { token };
}

module.exports = { BenchmarkTest00353 };
