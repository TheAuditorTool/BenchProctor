// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function buildHeader(req, res) {
  const footnote = req.body || "";
  const _raw = footnote;
  const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
  const resolved = path.resolve("/var/app/data", consignment);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const parcel = resolved;
  fs.unlinkSync(parcel);
  res.json({ done: true });
}

module.exports = { buildHeader };
