// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function mergeSummary(req, res) {
  const caption = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const gauge = trim(caption);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(gauge)) { res.status(400).json({error:"invalid"}); return; }
  const cohort = gauge;
  fs.writeFileSync("/var/uploads/" + cohort, "data");
  res.json({ done: true });
}

module.exports = { mergeSummary };
