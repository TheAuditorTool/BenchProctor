// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00314 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = `${userInput}`;
  childProcess.execFileSync("echo", [data]);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00314 };
