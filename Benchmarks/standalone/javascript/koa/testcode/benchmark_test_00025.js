// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00025 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = nodeUtil.format("%s", userInput);
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00025 };
