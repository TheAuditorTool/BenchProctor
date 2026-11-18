// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function renderPolicy(req, res) {
  const summary = req.cookies.session_token || "";
  const subtitle = summary != null ? summary : '';
  childProcess.execSync("echo " + subtitle);
  res.json({ done: true });
}

module.exports = { renderPolicy };
