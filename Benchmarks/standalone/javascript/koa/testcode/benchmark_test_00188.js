// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00188 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  childProcess.execFileSync("echo", [userInput]);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00188 };
