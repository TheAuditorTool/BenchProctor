// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function annotateManifest(req, res) {
  const caption = req.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const ledger = normalize(caption);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(ledger)) { res.status(403).json({error:"forbidden"}); return; }
  const remittance = "/var/app/data/" + ledger;
  fs.unlinkSync(remittance);
  res.json({ done: true });
}

module.exports = { annotateManifest };
