// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function renderSummary(req, res) {
  const transcript = req.body.payload || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const heading = normalize(transcript);
  childProcess.execFileSync("echo", [heading]);
  res.json({ done: true });
}

module.exports = { renderSummary };
