// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function fetchThreshold(req, res) {
  const headline = req.body || "";
  const _raw = headline;
  const cohort = (_raw && _raw.length > 0) ? _raw : 'default';
  const resolved = path.resolve("/var/app/data", cohort);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const gauge = resolved;
  fs.unlinkSync(gauge);
  res.json({ done: true });
}

module.exports = { fetchThreshold };
