// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function auditManifest(req, res) {
  const footnote = req.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const byline = normalize(footnote);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(byline)) { res.status(403).json({error:"forbidden"}); return; }
  const addendum = "/var/app/data/" + byline;
  fs.unlinkSync(addendum);
  res.json({ done: true });
}

module.exports = { auditManifest };
