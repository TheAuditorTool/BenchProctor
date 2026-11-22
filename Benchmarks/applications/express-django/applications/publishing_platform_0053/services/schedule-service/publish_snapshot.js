// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function publishSnapshot(req, res) {
  const note = req.headers.referer || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(note);
  const byline = readInput();
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(byline);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const addendum = _parsed.data;
  childProcess.exec("echo " + addendum, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { publishSnapshot };
