// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00225 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const [data] = String(userInput).split(',');
  childProcess.execSync("echo " + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00225 };
