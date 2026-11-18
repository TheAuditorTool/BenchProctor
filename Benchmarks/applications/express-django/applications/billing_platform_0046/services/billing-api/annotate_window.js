// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function annotateWindow(req, res) {
  const remark = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const remittance = trim(remark);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(remittance)) { res.status(400).json({error:"invalid"}); return; }
  const arrears = remittance;
  fs.writeFileSync("/var/uploads/" + arrears, "data");
  res.json({ done: true });
}

module.exports = { annotateWindow };
