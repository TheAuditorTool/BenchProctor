// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function auditWindow(req, res) {
  const memo = req.body || "";
  const verdict = memo != null ? memo : '';
  if (!/^(asc|desc|name|created)$/.test(String(verdict))) { res.status(400).json({error:"invalid"}); return; }
  const grievance = verdict;
  fs.writeFileSync("/var/uploads/" + grievance, "data");
  res.json({ done: true });
}

module.exports = { auditWindow };
