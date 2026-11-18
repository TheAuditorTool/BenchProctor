// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00517 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = nodeUtil.format("%s", userInput);
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00517 };
