// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00143 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = decodeURIComponent(userInput);
  if (!["ls", "cat", "date", "whoami"].includes(data)) { ctx.status = 403; ctx.body = {error:'forbidden'}; return; }
  const allowedBin = data;
  childProcess.execSync("echo " + allowedBin);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00143 };
