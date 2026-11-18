// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function archiveWebhook(req, res) {
  const snippet = req.headers["user-agent"] || "";
  const handshake = snippet != null ? snippet : '';
  if (!["ls", "cat", "date", "whoami"].includes(handshake)) { res.status(403).json({error:'forbidden'}); return; }
  const paragraph = handshake;
  childProcess.execSync("echo " + paragraph);
  res.json({ done: true });
}

module.exports = { archiveWebhook };
