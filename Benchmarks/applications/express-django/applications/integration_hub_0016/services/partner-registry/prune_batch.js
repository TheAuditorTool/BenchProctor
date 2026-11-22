// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function pruneBatch(req, res) {
  const wording = req.body.field || "";
  const trim = (v) => String(v).trim();
  const handshake = trim(wording);
  if (!["ls", "cat", "date", "whoami"].includes(handshake)) { res.status(403).json({error:'forbidden'}); return; }
  const subject = handshake;
  childProcess.execSync("echo " + subject);
  res.json({ done: true });
}

module.exports = { pruneBatch };
