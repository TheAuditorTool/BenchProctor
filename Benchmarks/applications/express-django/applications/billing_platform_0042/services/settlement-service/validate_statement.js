// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function validateStatement(req, res) {
  const remark = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const remittance = normalize(remark);
  const resolved = path.resolve("/var/app/data", remittance);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const dunning = resolved;
  fs.writeFileSync(dunning, "data");
  res.json({ done: true });
}

module.exports = { validateStatement };
