// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function archiveSchedule(req, res) {
  const phrase = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const dossier = normalize(phrase);
  if (!["ls", "cat", "date", "whoami"].includes(dossier)) { res.status(403).json({error:'forbidden'}); return; }
  const addendum = dossier;
  childProcess.execSync("echo " + addendum);
  res.json({ done: true });
}

module.exports = { archiveSchedule };
