// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function reconcileThreshold(req, res) {
  const remark = req.body || "";
  const gauge = remark != null ? remark : '';
  if (!/^(asc|desc|name|created)$/.test(String(gauge))) { res.status(400).json({error:"invalid"}); return; }
  const cohort = gauge;
  fs.writeFileSync("/var/uploads/" + cohort, "data");
  res.json({ done: true });
}

module.exports = { reconcileThreshold };
