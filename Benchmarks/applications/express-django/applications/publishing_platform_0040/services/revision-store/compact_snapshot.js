// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function compactSnapshot(req, res) {
  const transcript = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const addendum = normalize(transcript);
  if (!["ls", "cat", "date", "whoami"].includes(addendum)) { res.status(403).json({error:'forbidden'}); return; }
  const byline = addendum;
  childProcess.execSync("echo " + byline);
  res.json({ done: true });
}

module.exports = { compactSnapshot };
