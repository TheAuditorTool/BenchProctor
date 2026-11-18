// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function compactBatch(req, res) {
  const note = req.headers["user-agent"] || "";
  const handshake = note != null ? note : '';
  if (!["ls", "cat", "date", "whoami"].includes(handshake)) { res.status(403).json({error:'forbidden'}); return; }
  const persona = handshake;
  childProcess.execSync("echo " + persona);
  res.json({ done: true });
}

module.exports = { compactBatch };
