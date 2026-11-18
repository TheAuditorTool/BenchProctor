// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function verifyIndex(req, res) {
  const subject = req.body || "";
  const _raw = subject;
  const grievance = (_raw && _raw.length > 0) ? _raw : 'default';
  const resolved = path.resolve("/var/app/data", grievance);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const verdict = resolved;
  fs.unlinkSync(verdict);
  res.json({ done: true });
}

module.exports = { verifyIndex };
