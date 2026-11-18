// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function enrichConfig(req, res) {
  const summary = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const addendum = normalize(summary);
  const resolved = path.resolve("/var/app/data", addendum);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const byline = resolved;
  fs.writeFileSync(byline, "data");
  res.json({ done: true });
}

module.exports = { enrichConfig };
