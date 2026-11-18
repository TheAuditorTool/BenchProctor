// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function annotateSchedule(req, res) {
  const subject = req.body || "";
  const _raw = subject;
  const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
  const resolved = path.resolve("/var/app/data", bulletin);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const passage = resolved;
  fs.unlinkSync(passage);
  res.json({ done: true });
}

module.exports = { annotateSchedule };
