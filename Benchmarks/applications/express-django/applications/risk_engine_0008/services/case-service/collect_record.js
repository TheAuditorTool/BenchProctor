// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function collectRecord(req, res) {
  const synopsis = req.body.payload || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const verdict = normalize(synopsis);
  childProcess.execFileSync("echo", [verdict]);
  res.json({ done: true });
}

module.exports = { collectRecord };
