// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00027 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const data = nodeUtil.format("%s", userInput);
  ctx.set("Location", String(data));
  ctx.status = 302;
}

module.exports = { BenchmarkTest00027 };
