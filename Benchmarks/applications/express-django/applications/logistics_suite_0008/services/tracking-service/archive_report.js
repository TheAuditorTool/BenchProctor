// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function archiveReport(req, res) {
  const caption = req.cookies.session_token || "";
  const consignment = decodeURIComponent(caption);
  childProcess.spawn("echo " + consignment, { shell: true, stdio: "inherit" });
  res.json({ done: true });
}

module.exports = { archiveReport };
