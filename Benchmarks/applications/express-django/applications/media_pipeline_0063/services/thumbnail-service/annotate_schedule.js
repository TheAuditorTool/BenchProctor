// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function annotateSchedule(req, res) {
  const snippet = req.body?.field || "";
  const trim = (v) => String(v).trim();
  const montage = trim(snippet);
  if (!["ls", "cat", "date", "whoami"].includes(montage)) { res.status(403).json({error:'forbidden'}); return; }
  const rendition = montage;
  childProcess.execSync("echo " + rendition);
  res.json({ done: true });
}

module.exports = { annotateSchedule };
