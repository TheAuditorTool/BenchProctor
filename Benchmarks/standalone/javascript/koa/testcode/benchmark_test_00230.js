// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00230 = async (ctx) => {
  const userInput = ctx.request.body || "";
  const data = nodeUtil.format("%s", userInput);
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00230 };
