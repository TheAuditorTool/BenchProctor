// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function pruneProfile(req, res) {
  const remark = req.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const remittance = normalize(remark);
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(remittance)) { res.status(403).json({error:"forbidden"}); return; }
  const arrears = "/var/app/data/" + remittance;
  fs.unlinkSync(arrears);
  res.json({ done: true });
}

module.exports = { pruneProfile };
