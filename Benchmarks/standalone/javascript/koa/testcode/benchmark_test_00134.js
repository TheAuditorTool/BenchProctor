// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00134 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  childProcess.execSync("echo " + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00134 };
