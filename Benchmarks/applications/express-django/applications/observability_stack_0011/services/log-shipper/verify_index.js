// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function verifyIndex(req, res) {
  const caption = req.body || "";
  const _raw = caption;
  const gauge = (_raw && _raw.length > 0) ? _raw : 'default';
  const resolved = path.resolve("/var/app/data", gauge);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const cohort = resolved;
  fs.unlinkSync(cohort);
  res.json({ done: true });
}

module.exports = { verifyIndex };
