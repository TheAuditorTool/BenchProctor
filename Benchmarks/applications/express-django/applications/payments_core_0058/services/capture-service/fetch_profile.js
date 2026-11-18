// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function fetchProfile(req, res) {
  const caption = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const ledger = trim(caption);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(ledger)) { res.status(400).json({error:"invalid"}); return; }
  const remittance = ledger;
  fs.writeFileSync("/var/uploads/" + remittance, "data");
  res.json({ done: true });
}

module.exports = { fetchProfile };
