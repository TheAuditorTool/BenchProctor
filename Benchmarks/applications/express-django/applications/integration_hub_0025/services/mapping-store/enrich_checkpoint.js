// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function enrichCheckpoint(req, res) {
  const footnote = req.body.payload || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const handshake = normalize(footnote);
  childProcess.execFileSync("echo", [handshake]);
  res.json({ done: true });
}

module.exports = { enrichCheckpoint };
