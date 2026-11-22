// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function loadSummary(req, res) {
  const remark = req.headers.authorization || "";
  const [note] = String(remark).split(',');
  childProcess.execSync("echo " + note);
  res.json({ done: true });
}

module.exports = { loadSummary };
