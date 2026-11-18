// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function annotateManifest(req, res) {
  const tagline = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const rendition = normalize(tagline);
  const resolved = path.resolve("/var/app/data", rendition);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const montage = resolved;
  fs.writeFileSync(montage, "data");
  res.json({ done: true });
}

module.exports = { annotateManifest };
