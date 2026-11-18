// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function renderThreshold(req, res) {
  const citation = req.cookies.session_token || "";
  const grievance = citation != null ? citation : '';
  childProcess.execSync("echo " + grievance);
  res.json({ done: true });
}

module.exports = { renderThreshold };
