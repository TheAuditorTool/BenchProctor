// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00216 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const data = String(userInput).replace(/\u0000/g, "");
  childProcess.execSync("echo " + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00216 };
