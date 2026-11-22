// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00287 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = String(userInput).replace(/\u0000/g, "");
  childProcess.spawn("echo " + data, { shell: true, stdio: "inherit" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00287 };
