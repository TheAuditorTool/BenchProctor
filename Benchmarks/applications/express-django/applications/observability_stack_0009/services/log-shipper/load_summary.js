// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function loadSummary(req, res) {
  const summary = req.headers["user-agent"] || "";
  const gauge = summary != null ? summary : '';
  if (!["ls", "cat", "date", "whoami"].includes(gauge)) { res.status(403).json({error:'forbidden'}); return; }
  const cohort = gauge;
  childProcess.execSync("echo " + cohort);
  res.json({ done: true });
}

module.exports = { loadSummary };
