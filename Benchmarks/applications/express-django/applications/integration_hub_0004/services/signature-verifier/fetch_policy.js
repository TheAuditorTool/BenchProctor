// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function fetchPolicy(req, res) {
  const summary = req.body.field || "";
  const trim = (v) => String(v).trim();
  const handshake = trim(summary);
  if (!["ls", "cat", "date", "whoami"].includes(handshake)) { res.status(403).json({error:'forbidden'}); return; }
  const paragraph = handshake;
  childProcess.execSync("echo " + paragraph);
  res.json({ done: true });
}

module.exports = { fetchPolicy };
