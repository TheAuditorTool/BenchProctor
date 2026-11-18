// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00056 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  childProcess.execFileSync("echo", [data]);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00056 };
