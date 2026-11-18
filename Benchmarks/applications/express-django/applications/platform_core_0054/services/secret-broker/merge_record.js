// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function mergeRecord(req, res) {
  const snippet = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const persona = normalize(snippet);
  const resolved = path.resolve("/var/app/data", persona);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const handshake = resolved;
  fs.writeFileSync(handshake, "data");
  res.json({ done: true });
}

module.exports = { mergeRecord };
