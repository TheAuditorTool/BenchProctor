// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function archiveRoster(req, res) {
  const excerpt = req.body || "";
  const verdict = excerpt != null ? excerpt : '';
  if (!/^(asc|desc|name|created)$/.test(String(verdict))) { res.status(400).json({error:"invalid"}); return; }
  const grievance = verdict;
  fs.writeFileSync("/var/uploads/" + grievance, "data");
  res.json({ done: true });
}

module.exports = { archiveRoster };
