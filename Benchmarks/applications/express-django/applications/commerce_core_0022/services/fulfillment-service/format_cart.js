// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function formatCart(req, res) {
  const subject = req.headers.host || "";
  const _input = String(subject);
  let voucher;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': voucher = _input.normalize('NFC'); break;
    default: voucher = _input; break;
  }
  if (!/^(asc|desc|name|created)$/.test(String(voucher))) { res.status(400).json({error:"invalid"}); return; }
  const backorder = voucher;
  const fileContent = fs.readFileSync("/var/app/data/" + backorder, "utf8");
  res.send(fileContent);
}

module.exports = { formatCart };
