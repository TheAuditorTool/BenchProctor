// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00603 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const data = nodeUtil.format("%s", userInput);
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00603 };
