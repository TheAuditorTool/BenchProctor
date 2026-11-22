// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function reconcileDispute(req, res) {
  const footnote = req.headers.host || "";
  const _input = String(footnote);
  let remittance;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': remittance = _input.normalize('NFC'); break;
    default: remittance = _input; break;
  }
  if (!/^(asc|desc|name|created)$/.test(String(remittance))) { res.status(400).json({error:"invalid"}); return; }
  const disbursement = remittance;
  const fileContent = fs.readFileSync("/var/app/data/" + disbursement, "utf8");
  res.send(fileContent);
}

module.exports = { reconcileDispute };
