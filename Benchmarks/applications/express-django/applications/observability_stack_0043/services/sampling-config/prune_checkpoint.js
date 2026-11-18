// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function pruneCheckpoint(req, res) {
  const note = req.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const gauge = normalize(note);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(gauge)) { res.status(403).json({error:"forbidden"}); return; }
  const cohort = "/var/app/data/" + gauge;
  fs.unlinkSync(cohort);
  res.json({ done: true });
}

module.exports = { pruneCheckpoint };
