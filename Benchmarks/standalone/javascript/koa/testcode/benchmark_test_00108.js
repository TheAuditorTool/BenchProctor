// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00108 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  childProcess.execSync("echo " + data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00108 };
