// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function publishSnapshot(req, res) {
  const heading = req.headers.referer || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const handshake = normalize(heading);
  childProcess.exec("echo " + handshake, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { publishSnapshot };
