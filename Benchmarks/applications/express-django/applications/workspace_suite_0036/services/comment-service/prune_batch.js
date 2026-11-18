// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function pruneBatch(req, res) {
  const remark = req.headers["user-agent"] || "";
  const synopsis = remark != null ? remark : '';
  if (!["ls", "cat", "date", "whoami"].includes(synopsis)) { res.status(403).json({error:'forbidden'}); return; }
  const quotation = synopsis;
  childProcess.execSync("echo " + quotation);
  res.json({ done: true });
}

module.exports = { pruneBatch };
