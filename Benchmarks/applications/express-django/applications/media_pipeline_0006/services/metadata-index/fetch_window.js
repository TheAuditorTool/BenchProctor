// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function fetchWindow(req, res) {
  const passage = req.body || "";
  const _raw = passage;
  const montage = (_raw && _raw.length > 0) ? _raw : 'default';
  const resolved = path.resolve("/var/app/data", montage);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const rendition = resolved;
  fs.unlinkSync(rendition);
  res.json({ done: true });
}

module.exports = { fetchWindow };
