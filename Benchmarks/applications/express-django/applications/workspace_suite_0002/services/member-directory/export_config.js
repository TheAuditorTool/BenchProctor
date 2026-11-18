// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function exportConfig(req, res) {
  const transcript = req.body || "";
  const _raw = transcript;
  const heading = (_raw && _raw.length > 0) ? _raw : 'default';
  const resolved = path.resolve("/var/app/data", heading);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const passage = resolved;
  fs.unlinkSync(passage);
  res.json({ done: true });
}

module.exports = { exportConfig };
