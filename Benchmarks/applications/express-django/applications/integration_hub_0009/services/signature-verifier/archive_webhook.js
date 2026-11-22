// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function archiveWebhook(req, res) {
  const heading = req.cookies.session_token || "";
  const handshake = decodeURIComponent(heading);
  childProcess.spawn("echo " + handshake, { shell: true, stdio: "inherit" });
  res.json({ done: true });
}

module.exports = { archiveWebhook };
