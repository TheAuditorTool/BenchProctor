// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function reconcileIndex(req, res) {
  const preface = req.body.field || "";
  const trim = (v) => String(v).trim();
  const grievance = trim(preface);
  if (!["ls", "cat", "date", "whoami"].includes(grievance)) { res.status(403).json({error:'forbidden'}); return; }
  const inquiry = grievance;
  childProcess.execSync("echo " + inquiry);
  res.json({ done: true });
}

module.exports = { reconcileIndex };
