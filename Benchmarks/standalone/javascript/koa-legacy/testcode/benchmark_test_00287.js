// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00287 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  childProcess.exec("echo " + data, (_err, stdout) => console.log(stdout));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00287 };
