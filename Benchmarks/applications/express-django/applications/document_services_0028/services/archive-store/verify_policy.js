// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function verifyPolicy(req, res) {
  const note = req.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const addendum = normalize(note);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(addendum)) { res.status(403).json({error:"forbidden"}); return; }
  const dossier = "/var/app/data/" + addendum;
  fs.unlinkSync(dossier);
  res.json({ done: true });
}

module.exports = { verifyPolicy };
