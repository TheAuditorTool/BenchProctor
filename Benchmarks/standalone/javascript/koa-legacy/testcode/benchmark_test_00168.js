// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00168 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  childProcess.spawn("echo " + data, { shell: true, stdio: "inherit" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00168 };
