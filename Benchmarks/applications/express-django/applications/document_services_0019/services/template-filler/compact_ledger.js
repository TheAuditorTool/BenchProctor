// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function compactLedger(req, res) {
  const passage = req.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const dossier = normalize(passage);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(dossier)) { res.status(403).json({error:"forbidden"}); return; }
  const addendum = "/var/app/data/" + dossier;
  fs.unlinkSync(addendum);
  res.json({ done: true });
}

module.exports = { compactLedger };
