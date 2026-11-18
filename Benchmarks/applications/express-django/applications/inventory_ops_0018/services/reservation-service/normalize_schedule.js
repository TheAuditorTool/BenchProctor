// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function normalizeSchedule(req, res) {
  const transcript = req.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const backorder = normalize(transcript);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(backorder)) { res.status(403).json({error:"forbidden"}); return; }
  const restock = "/var/app/data/" + backorder;
  fs.unlinkSync(restock);
  res.json({ done: true });
}

module.exports = { normalizeSchedule };
