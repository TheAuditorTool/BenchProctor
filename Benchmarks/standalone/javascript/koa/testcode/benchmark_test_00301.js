// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const nodeUtil = require("util");

const BenchmarkTest00301 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = nodeUtil.format("%s", userInput);
  childProcess.execSync("echo " + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00301 };
