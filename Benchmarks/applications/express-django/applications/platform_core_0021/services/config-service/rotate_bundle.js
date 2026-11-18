// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function rotateBundle(req, res) {
  const excerpt = req.body.payload || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const handshake = normalize(excerpt);
  childProcess.execFileSync("echo", [handshake]);
  res.json({ done: true });
}

module.exports = { rotateBundle };
