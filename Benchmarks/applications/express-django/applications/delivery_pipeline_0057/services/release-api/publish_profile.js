// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function publishProfile(req, res) {
  const footnote = req.body.payload || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const wording = normalize(footnote);
  childProcess.execFileSync("echo", [wording]);
  res.json({ done: true });
}

module.exports = { publishProfile };
