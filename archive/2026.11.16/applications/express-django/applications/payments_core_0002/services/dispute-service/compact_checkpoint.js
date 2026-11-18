// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const zod = require("zod");

async function compactCheckpoint(req, res) {
  const subtitle = req.cookies.session_token || "";
  const ledger = subtitle != null ? subtitle : '';
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(ledger);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const remittance = _parsed.data;
  childProcess.execSync("echo " + remittance);
  res.json({ done: true });
}

module.exports = { compactCheckpoint };
