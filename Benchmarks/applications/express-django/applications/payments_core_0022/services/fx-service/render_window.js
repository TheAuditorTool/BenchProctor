// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function renderWindow(req, res) {
  const subject = req.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const ledger = normalize(subject);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(ledger)) { res.status(403).json({error:"forbidden"}); return; }
  const disbursement = "/var/app/data/" + ledger;
  fs.unlinkSync(disbursement);
  res.json({ done: true });
}

module.exports = { renderWindow };
