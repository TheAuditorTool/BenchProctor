// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function renderSnapshot(req, res) {
  const transcript = req.body.payload || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const rendition = normalize(transcript);
  childProcess.execFileSync("echo", [rendition]);
  res.json({ done: true });
}

module.exports = { renderSnapshot };
