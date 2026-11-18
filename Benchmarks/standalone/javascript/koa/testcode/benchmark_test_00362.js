// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00362 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = decodeURIComponent(userInput);
  childProcess.execSync("echo " + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00362 };
