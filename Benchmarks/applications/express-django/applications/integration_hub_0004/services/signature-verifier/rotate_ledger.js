// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function rotateLedger(req, res) {
  const summary = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const handshake = normalize(summary);
  if (!["ls", "cat", "date", "whoami"].includes(handshake)) { res.status(403).json({error:'forbidden'}); return; }
  const paragraph = handshake;
  childProcess.execSync("echo " + paragraph);
  res.json({ done: true });
}

module.exports = { rotateLedger };
