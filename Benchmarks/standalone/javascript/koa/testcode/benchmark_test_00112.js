// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00112 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  childProcess.execSync("echo " + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00112 };
