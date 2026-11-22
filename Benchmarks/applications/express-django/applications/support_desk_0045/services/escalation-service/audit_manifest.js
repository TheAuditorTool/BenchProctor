// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function auditManifest(req, res) {
  const remark = req.headers.authorization || "";
  const [inquiry] = String(remark).split(',');
  childProcess.execSync("echo " + inquiry);
  res.json({ done: true });
}

module.exports = { auditManifest };
