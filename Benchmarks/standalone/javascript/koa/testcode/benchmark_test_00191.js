// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00191 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  childProcess.execSync("echo " + processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00191 };
