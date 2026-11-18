// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function renderReport(req, res) {
  const caption = req.headers["user-agent"] || "";
  const cohort = caption != null ? caption : '';
  if (!["ls", "cat", "date", "whoami"].includes(cohort)) { res.status(403).json({error:'forbidden'}); return; }
  const gauge = cohort;
  childProcess.execSync("echo " + gauge);
  res.json({ done: true });
}

module.exports = { renderReport };
