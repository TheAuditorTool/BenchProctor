// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00302 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const data = nodeUtil.format("%s", userInput);
  ctx.app.context.announcement = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00302 };
