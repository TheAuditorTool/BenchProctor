// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function BenchmarkTest00137(req, res) {
  const userInput = req.body.payload || "";
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(userInput);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const processed = _parsed.data;
  childProcess.exec("echo " + processed, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00137 };
