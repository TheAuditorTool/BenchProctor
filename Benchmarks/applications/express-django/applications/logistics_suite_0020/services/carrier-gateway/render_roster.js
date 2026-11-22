// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function renderRoster(req, res) {
  const transcript = req.cookies.session_token || "";
  const consignment = decodeURIComponent(transcript);
  childProcess.spawn("echo " + consignment, { shell: true, stdio: "inherit" });
  res.json({ done: true });
}

module.exports = { renderRoster };
