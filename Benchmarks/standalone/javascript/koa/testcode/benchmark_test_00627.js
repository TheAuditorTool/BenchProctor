// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00627 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  childProcess.execSync("echo " + processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00627 };
