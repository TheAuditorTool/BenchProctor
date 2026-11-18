// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const nodeUtil = require("util");

const BenchmarkTest00682 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const data = nodeUtil.format("%s", userInput);
  childProcess.execFileSync("echo", [data]);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00682 };
