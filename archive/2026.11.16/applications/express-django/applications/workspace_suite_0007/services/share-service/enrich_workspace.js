// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function enrichWorkspace(req, res) {
  const summary = req.cookies.session_token || "";
  const subtitle = summary != null ? summary : '';
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(subtitle);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const notice = _parsed.data;
  childProcess.execSync("echo " + notice);
  res.json({ done: true });
}

module.exports = { enrichWorkspace };
