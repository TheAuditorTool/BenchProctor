// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function publishReport(req, res) {
  const footnote = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const handshake = normalize(footnote);
  const resolved = path.resolve("/var/app/data", handshake);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const blurb = resolved;
  fs.writeFileSync(blurb, "data");
  res.json({ done: true });
}

module.exports = { publishReport };
