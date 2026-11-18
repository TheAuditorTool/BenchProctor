// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function mergeConversion(req, res) {
  const note = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const addendum = normalize(note);
  const resolved = path.resolve("/var/app/data", addendum);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const dossier = resolved;
  fs.writeFileSync(dossier, "data");
  res.json({ done: true });
}

module.exports = { mergeConversion };
