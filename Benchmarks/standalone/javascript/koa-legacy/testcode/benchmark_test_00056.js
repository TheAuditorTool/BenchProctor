// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

const BenchmarkTest00056 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(data);
  if (!_parsed.success) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = _parsed.data;
  childProcess.exec("echo " + processed, (_err, stdout) => console.log(stdout));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00056 };
