// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function archiveConfig(req, res) {
  const footnote = req.body.field || "";
  const trim = (v) => String(v).trim();
  const bulletin = trim(footnote);
  if (!["ls", "cat", "date", "whoami"].includes(bulletin)) { res.status(403).json({error:'forbidden'}); return; }
  const snippet = bulletin;
  childProcess.execSync("echo " + snippet);
  res.json({ done: true });
}

module.exports = { archiveConfig };
