// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function compactSchedule(req, res) {
  const paragraph = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const wording = normalize(paragraph);
  if (!["ls", "cat", "date", "whoami"].includes(wording)) { res.status(403).json({error:'forbidden'}); return; }
  const transcript = wording;
  childProcess.execSync("echo " + transcript);
  res.json({ done: true });
}

module.exports = { compactSchedule };
