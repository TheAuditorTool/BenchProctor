// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function loadPolicy(req, res) {
  const summary = req.body.field || "";
  const trim = (v) => String(v).trim();
  const phrase = trim(summary);
  if (!["ls", "cat", "date", "whoami"].includes(phrase)) { res.status(403).json({error:'forbidden'}); return; }
  const subtitle = phrase;
  childProcess.execSync("echo " + subtitle);
  res.json({ done: true });
}

module.exports = { loadPolicy };
