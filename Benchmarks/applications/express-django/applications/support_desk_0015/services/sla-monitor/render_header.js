// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function renderHeader(req, res) {
  const phrase = req.headers.referer || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(phrase);
  const grievance = readInput();
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(grievance);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const inquiry = _parsed.data;
  childProcess.exec("echo " + inquiry, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { renderHeader };
