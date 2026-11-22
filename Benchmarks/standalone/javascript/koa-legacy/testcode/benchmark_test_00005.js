// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const nodeUtil = require("util");

const BenchmarkTest00005 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const data = nodeUtil.format("%s", userInput);
  childProcess.exec("echo " + data, (_err, stdout) => console.log(stdout));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00005 };
