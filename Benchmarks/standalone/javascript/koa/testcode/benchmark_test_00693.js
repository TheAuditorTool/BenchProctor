// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00693 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const data = decodeURIComponent(userInput);
  childProcess.execFileSync("echo", [data]);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00693 };
