// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00153 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!["ls", "cat", "date", "whoami"].includes(data)) { ctx.status = 403; ctx.body = {error:'forbidden'}; return; }
  const allowedBin = data;
  childProcess.spawn("echo " + allowedBin, { shell: true, stdio: "inherit" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00153 };
