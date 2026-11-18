// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function fetchRoster(req, res) {
  const synopsis = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const byline = normalize(synopsis);
  const resolved = path.resolve("/var/app/data", byline);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const addendum = resolved;
  fs.writeFileSync(addendum, "data");
  res.json({ done: true });
}

module.exports = { fetchRoster };
