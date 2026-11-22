// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00013 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const [data] = String(userInput).split(',');
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  childProcess.spawn("echo " + processed, { shell: true, stdio: "inherit" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00013 };
