// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function enrichBundle(req, res) {
  const note = req.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const inquiry = normalize(note);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(inquiry)) { res.status(403).json({error:"forbidden"}); return; }
  const grievance = "/var/app/data/" + inquiry;
  fs.unlinkSync(grievance);
  res.json({ done: true });
}

module.exports = { enrichBundle };
