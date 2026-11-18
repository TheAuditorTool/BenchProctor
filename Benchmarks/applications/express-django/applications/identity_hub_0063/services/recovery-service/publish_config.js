// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function publishConfig(req, res) {
  const paragraph = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const persona = normalize(paragraph);
  const resolved = path.resolve("/var/app/data", persona);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const synopsis = resolved;
  fs.writeFileSync(synopsis, "data");
  res.json({ done: true });
}

module.exports = { publishConfig };
