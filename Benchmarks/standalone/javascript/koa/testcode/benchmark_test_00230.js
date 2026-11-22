// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00230 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  childProcess.execFile("echo", [String(data)], (_err, stdout) => console.log(stdout));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00230 };
