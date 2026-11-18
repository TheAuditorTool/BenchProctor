// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00113 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = Buffer.from(userInput, "hex").toString();
  childProcess.execFileSync("echo", [data]);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00113 };
