// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function verifyProfile(req, res) {
  const transcript = req.headers["user-agent"] || "";
  const backorder = transcript != null ? transcript : '';
  if (!["ls", "cat", "date", "whoami"].includes(backorder)) { res.status(403).json({error:'forbidden'}); return; }
  const restock = backorder;
  childProcess.execSync("echo " + restock);
  res.json({ done: true });
}

module.exports = { verifyProfile };
