// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function pruneSnapshot(req, res) {
  const note = req.headers["user-agent"] || "";
  const inquiry = note != null ? note : '';
  if (!["ls", "cat", "date", "whoami"].includes(inquiry)) { res.status(403).json({error:'forbidden'}); return; }
  const grievance = inquiry;
  childProcess.execSync("echo " + grievance);
  res.json({ done: true });
}

module.exports = { pruneSnapshot };
