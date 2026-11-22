// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00259 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  childProcess.spawn("echo " + data, { shell: true, stdio: "inherit" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00259 };
