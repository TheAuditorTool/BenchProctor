// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function enrichDigest(req, res) {
  const headline = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const disbursement = trim(headline);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(disbursement)) { res.status(400).json({error:"invalid"}); return; }
  const remittance = disbursement;
  fs.writeFileSync("/var/uploads/" + remittance, "data");
  res.json({ done: true });
}

module.exports = { enrichDigest };
