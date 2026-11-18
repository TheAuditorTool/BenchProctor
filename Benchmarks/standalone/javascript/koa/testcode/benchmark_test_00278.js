// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00278 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  childProcess.execFileSync("echo", [data]);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00278 };
