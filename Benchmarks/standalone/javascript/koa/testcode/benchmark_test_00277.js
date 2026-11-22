// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00277 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  childProcess.exec("echo " + data, (_err, stdout) => console.log(stdout));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00277 };
