// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00358 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  childProcess.execSync("echo " + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00358 };
