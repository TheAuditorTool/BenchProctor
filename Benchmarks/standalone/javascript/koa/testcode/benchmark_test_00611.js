// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

const BenchmarkTest00611 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(userInput);
  if (!_parsed.success) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = _parsed.data;
  childProcess.execSync("echo " + processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00611 };
