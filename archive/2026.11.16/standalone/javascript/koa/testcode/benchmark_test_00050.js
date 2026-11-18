// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const nodeUtil = require("util");

const BenchmarkTest00050 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const data = nodeUtil.format("%s", userInput);
  childProcess.execSync("echo " + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00050 };
