// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function mergeIndex(req, res) {
  const subtitle = req.headers.authorization || "";
  let ledger;
  try { ledger = JSON.parse(subtitle).value || subtitle; }
  catch (e) { ledger = subtitle; }
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(ledger)) { res.status(400).json({error:"invalid"}); return; }
  const remittance = ledger;
  fs.unlinkSync("/var/app/data/" + remittance);
  res.json({ done: true });
}

module.exports = { mergeIndex };
