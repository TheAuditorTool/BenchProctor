// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

const BenchmarkTest00253 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = userInput != null ? userInput : '';
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(data);
  if (!_parsed.success) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = _parsed.data;
  childProcess.execSync("echo " + processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00253 };
