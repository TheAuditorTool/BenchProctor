// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00664 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const data = userInput != null ? userInput : '';
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  childProcess.execSync("echo " + processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00664 };
