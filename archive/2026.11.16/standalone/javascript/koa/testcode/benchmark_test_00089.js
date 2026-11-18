// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

const BenchmarkTest00089 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  childProcess.execSync("echo " + processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00089 };
