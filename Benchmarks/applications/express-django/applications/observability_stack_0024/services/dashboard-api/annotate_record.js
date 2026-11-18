// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function annotateRecord(req, res) {
  const summary = req.headers.authorization || "";
  const tokens = String(summary).split(',').filter((t) => t.length > 0);
  const cohort = tokens.join(' ');
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(cohort);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const gauge = _parsed.data;
  childProcess.execSync("echo " + gauge);
  res.json({ done: true });
}

module.exports = { annotateRecord };
