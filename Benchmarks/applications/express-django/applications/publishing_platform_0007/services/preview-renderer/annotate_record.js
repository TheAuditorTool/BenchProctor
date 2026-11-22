// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function annotateRecord(req, res) {
  const remark = req.body || "";
  const byline = remark != null ? remark : '';
  if (!/^(asc|desc|name|created)$/.test(String(byline))) { res.status(400).json({error:"invalid"}); return; }
  const addendum = byline;
  fs.writeFileSync("/var/uploads/" + addendum, "data");
  res.json({ done: true });
}

module.exports = { annotateRecord };
