// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00211 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  childProcess.spawn("echo " + data, { shell: true, stdio: "inherit" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00211 };
