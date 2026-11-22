// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00274 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  if (!["ls", "cat", "date", "whoami"].includes(data)) { ctx.status = 403; ctx.body = {error:'forbidden'}; return; }
  const allowedBin = data;
  childProcess.exec("echo " + allowedBin, (_err, stdout) => console.log(stdout));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00274 };
