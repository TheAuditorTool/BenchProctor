// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function enrichRoster(req, res) {
  const passage = req.headers.authorization || "";
  let remittance;
  try { remittance = JSON.parse(passage).value || passage; }
  catch (e) { remittance = passage; }
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(remittance)) { res.status(400).json({error:"invalid"}); return; }
  const disbursement = remittance;
  fs.unlinkSync("/var/app/data/" + disbursement);
  res.json({ done: true });
}

module.exports = { enrichRoster };
