// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function mergeReport(req, res) {
  const subtitle = req.cookies.session_token || "";
  const persona = decodeURIComponent(subtitle);
  childProcess.spawn("echo " + persona, { shell: true, stdio: "inherit" });
  res.json({ done: true });
}

module.exports = { mergeReport };
