// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00423 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = nodeUtil.format("%s", userInput);
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00423 };
