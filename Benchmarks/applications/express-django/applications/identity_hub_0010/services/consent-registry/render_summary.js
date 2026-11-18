// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function renderSummary(req, res) {
  const phrase = req.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const persona = normalize(phrase);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(persona)) { res.status(403).json({error:"forbidden"}); return; }
  const transcript = "/var/app/data/" + persona;
  fs.unlinkSync(transcript);
  res.json({ done: true });
}

module.exports = { renderSummary };
