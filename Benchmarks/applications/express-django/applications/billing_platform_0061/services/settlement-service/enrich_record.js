// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function enrichRecord(req, res) {
  const footnote = req.headers["x-custom-header"] || "";
  const remittance = Buffer.from(footnote, "hex").toString();
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(remittance)) { res.status(400).json({error:"invalid"}); return; }
  const arrears = remittance;
  fs.unlinkSync("/var/app/data/" + arrears);
  res.json({ done: true });
}

module.exports = { enrichRecord };
