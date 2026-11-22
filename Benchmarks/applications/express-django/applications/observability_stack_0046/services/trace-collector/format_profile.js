// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function formatProfile(req, res) {
  const paragraph = req.headers.referer || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(paragraph);
  const gauge = readInput();
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(gauge);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const cohort = _parsed.data;
  childProcess.exec("echo " + cohort, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { formatProfile };
