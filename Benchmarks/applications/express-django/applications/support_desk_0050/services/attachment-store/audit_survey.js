// SPDX-License-Identifier: Apache-2.0
const path = require("path");
const fs = require("fs");

async function auditSurvey(req, res) {
  const remark = req.body || "";
  const _raw = remark;
  const inquiry = (_raw && _raw.length > 0) ? _raw : 'default';
  const resolved = path.resolve("/var/app/data", inquiry);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const grievance = resolved;
  fs.unlinkSync(grievance);
  res.json({ done: true });
}

module.exports = { auditSurvey };
