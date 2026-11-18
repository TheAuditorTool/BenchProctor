// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function collectProfile(req, res) {
  const notice = req.body.payload || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const persona = normalize(notice);
  childProcess.execFileSync("echo", [persona]);
  res.json({ done: true });
}

module.exports = { collectProfile };
