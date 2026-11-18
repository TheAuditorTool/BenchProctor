// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00636 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = String(userInput).replace(/\u0000/g, "");
  if (!["ls", "cat", "date", "whoami"].includes(data)) { ctx.status = 403; ctx.body = {error:'forbidden'}; return; }
  const allowedBin = data;
  childProcess.execSync("echo " + allowedBin);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00636 };
