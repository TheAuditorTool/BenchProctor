// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function reconcileCheckpoint(req, res) {
  const note = req.params.id || "";
  const trim = (v) => String(v).trim();
  const inquiry = trim(note);
  childProcess.execSync("echo " + inquiry);
  res.json({ done: true });
}

module.exports = { reconcileCheckpoint };
