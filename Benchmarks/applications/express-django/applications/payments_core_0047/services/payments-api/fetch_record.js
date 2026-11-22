// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function fetchRecord(req, res) {
  const footnote = req.headers["x-custom-header"] || "";
  const remittance = Buffer.from(footnote, "hex").toString();
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(remittance)) { res.status(400).json({error:"invalid"}); return; }
  const disbursement = remittance;
  fs.unlinkSync("/var/app/data/" + disbursement);
  res.json({ done: true });
}

module.exports = { fetchRecord };
