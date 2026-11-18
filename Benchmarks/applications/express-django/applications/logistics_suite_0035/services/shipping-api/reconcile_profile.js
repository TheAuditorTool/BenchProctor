// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function reconcileProfile(req, res) {
  const phrase = req.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const parcel = normalize(phrase);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(parcel)) { res.status(403).json({error:"forbidden"}); return; }
  const consignment = "/var/app/data/" + parcel;
  fs.unlinkSync(consignment);
  res.json({ done: true });
}

module.exports = { reconcileProfile };
