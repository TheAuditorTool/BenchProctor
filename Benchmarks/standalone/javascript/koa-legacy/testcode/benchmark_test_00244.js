// SPDX-License-Identifier: Apache-2.0
const net = require("net");
const nodeUtil = require("util");

const BenchmarkTest00244 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = nodeUtil.format("%s", userInput);
  net.connect(80, new URL(String(data)).hostname);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00244 };
