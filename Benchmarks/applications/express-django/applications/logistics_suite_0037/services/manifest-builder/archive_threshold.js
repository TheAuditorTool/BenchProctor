// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function archiveThreshold(req, res) {
  const footnote = req.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const consignment = normalize(footnote);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(consignment)) { res.status(403).json({error:"forbidden"}); return; }
  const parcel = "/var/app/data/" + consignment;
  fs.unlinkSync(parcel);
  res.json({ done: true });
}

module.exports = { archiveThreshold };
