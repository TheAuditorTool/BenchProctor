// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00354 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  childProcess.spawn("echo " + data, { shell: true, stdio: "inherit" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00354 };
