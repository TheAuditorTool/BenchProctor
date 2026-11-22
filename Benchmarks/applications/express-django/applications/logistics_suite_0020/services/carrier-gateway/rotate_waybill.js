// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function rotateWaybill(req, res) {
  const transcript = req.headers.host || "";
  const _input = String(transcript);
  let consignment;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': consignment = _input.normalize('NFC'); break;
    default: consignment = _input; break;
  }
  if (!/^(asc|desc|name|created)$/.test(String(consignment))) { res.status(400).json({error:"invalid"}); return; }
  const parcel = consignment;
  const fileContent = fs.readFileSync("/var/app/data/" + parcel, "utf8");
  res.send(fileContent);
}

module.exports = { rotateWaybill };
