// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function summarizeRoster(req, res) {
  const preface = req.body || "";
  const grievance = preface != null ? preface : '';
  if (!/^(asc|desc|name|created)$/.test(String(grievance))) { res.status(400).json({error:"invalid"}); return; }
  const inquiry = grievance;
  fs.writeFileSync("/var/uploads/" + inquiry, "data");
  res.json({ done: true });
}

module.exports = { summarizeRoster };
