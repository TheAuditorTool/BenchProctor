// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function BenchmarkTest00194(req, res) {
  const userInput = req.body.field || "";
  const data = userInput != null ? userInput : '';
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(data);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const processed = _parsed.data;
  childProcess.execSync("echo " + processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00194 };
