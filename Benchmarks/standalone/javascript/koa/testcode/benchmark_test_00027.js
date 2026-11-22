// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00027 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = nodeUtil.format("%s", userInput);
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00027 };
