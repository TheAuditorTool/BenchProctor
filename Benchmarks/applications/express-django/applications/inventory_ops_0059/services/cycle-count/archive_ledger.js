// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function archiveLedger(req, res) {
  const memo = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const backorder = normalize(memo);
  if (!["ls", "cat", "date", "whoami"].includes(backorder)) { res.status(403).json({error:'forbidden'}); return; }
  const restock = backorder;
  childProcess.execSync("echo " + restock);
  res.json({ done: true });
}

module.exports = { archiveLedger };
