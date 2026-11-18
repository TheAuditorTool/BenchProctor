// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00024 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const data = nodeUtil.format("%s", userInput);
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00024 };
