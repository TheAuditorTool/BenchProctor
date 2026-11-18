// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function pruneBatch(req, res) {
  const summary = req.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const grievance = normalize(summary);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(grievance)) { res.status(403).json({error:"forbidden"}); return; }
  const verdict = "/var/app/data/" + grievance;
  fs.unlinkSync(verdict);
  res.json({ done: true });
}

module.exports = { pruneBatch };
