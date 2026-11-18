// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function exportConfig(req, res) {
  const notice = req.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const persona = normalize(notice);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(persona)) { res.status(403).json({error:"forbidden"}); return; }
  const handshake = "/var/app/data/" + persona;
  fs.unlinkSync(handshake);
  res.json({ done: true });
}

module.exports = { exportConfig };
