// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function archiveIndex(req, res) {
  const excerpt = req.body.field || "";
  const trim = (v) => String(v).trim();
  const cohort = trim(excerpt);
  if (!["ls", "cat", "date", "whoami"].includes(cohort)) { res.status(403).json({error:'forbidden'}); return; }
  const gauge = cohort;
  childProcess.execSync("echo " + gauge);
  res.json({ done: true });
}

module.exports = { archiveIndex };
