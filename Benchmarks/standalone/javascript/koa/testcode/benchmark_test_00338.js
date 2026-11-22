// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00338 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  childProcess.execSync("echo " + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00338 };
