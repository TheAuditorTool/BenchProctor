// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function renderLedger(req, res) {
  const remark = req.headers["user-agent"] || "";
  const trim = (v) => String(v).trim();
  const byline = trim(remark);
  childProcess.exec("echo " + byline, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { renderLedger };
