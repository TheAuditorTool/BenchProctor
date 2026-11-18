// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00047 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const [data] = String(userInput).split(',');
  childProcess.execSync("echo " + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00047 };
