// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function auditReport(req, res) {
  const remark = req.headers["user-agent"] || "";
  const trim = (v) => String(v).trim();
  const persona = trim(remark);
  childProcess.exec("echo " + persona, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { auditReport };
