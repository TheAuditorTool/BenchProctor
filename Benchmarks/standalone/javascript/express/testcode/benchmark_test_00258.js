// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function BenchmarkTest00258(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(userInput);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const processed = _parsed.data;
  childProcess.execSync("echo " + processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00258 };
