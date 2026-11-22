// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function fetchBatch(req, res) {
  const snippet = req.headers.host || "";
  const _input = String(snippet);
  let inquiry;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': inquiry = _input.normalize('NFC'); break;
    default: inquiry = _input; break;
  }
  if (!/^(asc|desc|name|created)$/.test(String(inquiry))) { res.status(400).json({error:"invalid"}); return; }
  const grievance = inquiry;
  const fileContent = fs.readFileSync("/var/app/data/" + grievance, "utf8");
  res.send(fileContent);
}

module.exports = { fetchBatch };
