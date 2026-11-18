// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00657 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const data = Buffer.from(userInput, "hex").toString();
  childProcess.execSync("echo " + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00657 };
