// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function pruneRecord(req, res) {
  const remark = req.headers["user-agent"] || "";
  const remittance = remark != null ? remark : '';
  if (!["ls", "cat", "date", "whoami"].includes(remittance)) { res.status(403).json({error:'forbidden'}); return; }
  const arrears = remittance;
  childProcess.execSync("echo " + arrears);
  res.json({ done: true });
}

module.exports = { pruneRecord };
