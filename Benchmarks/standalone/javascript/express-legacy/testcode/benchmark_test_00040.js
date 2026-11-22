// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function BenchmarkTest00040(req, res) {
  const userInput = req.params.id || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(data);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const processed = _parsed.data;
  childProcess.exec("echo " + processed, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00040 };
