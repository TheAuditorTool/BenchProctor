// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function loadBundle(req, res) {
  const notice = req.headers.host || "";
  const _input = String(notice);
  let backorder;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': backorder = _input.normalize('NFC'); break;
    default: backorder = _input; break;
  }
  if (!/^(asc|desc|name|created)$/.test(String(backorder))) { res.status(400).json({error:"invalid"}); return; }
  const voucher = backorder;
  const fileContent = fs.readFileSync("/var/app/data/" + voucher, "utf8");
  res.send(fileContent);
}

module.exports = { loadBundle };
