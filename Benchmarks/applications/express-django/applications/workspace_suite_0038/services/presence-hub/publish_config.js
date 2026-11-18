// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function publishConfig(req, res) {
  const preface = req.headers["user-agent"] || "";
  const remark = preface != null ? preface : '';
  if (!["ls", "cat", "date", "whoami"].includes(remark)) { res.status(403).json({error:'forbidden'}); return; }
  const wording = remark;
  childProcess.execSync("echo " + wording);
  res.json({ done: true });
}

module.exports = { publishConfig };
