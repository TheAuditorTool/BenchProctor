// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00537 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const data = `${userInput}`;
  childProcess.execSync("echo " + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00537 };
