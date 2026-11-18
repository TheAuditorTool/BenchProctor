// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function reconcileRoster(req, res) {
  const caption = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const cohort = trim(caption);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(cohort)) { res.status(400).json({error:"invalid"}); return; }
  const gauge = cohort;
  fs.writeFileSync("/var/uploads/" + gauge, "data");
  res.json({ done: true });
}

module.exports = { reconcileRoster };
