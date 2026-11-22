// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function resolveIndex(req, res) {
  const preface = req.headers.host || "";
  const _input = String(preface);
  let grievance;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': grievance = _input.normalize('NFC'); break;
    default: grievance = _input; break;
  }
  if (!/^(asc|desc|name|created)$/.test(String(grievance))) { res.status(400).json({error:"invalid"}); return; }
  const inquiry = grievance;
  const fileContent = fs.readFileSync("/var/app/data/" + inquiry, "utf8");
  res.send(fileContent);
}

module.exports = { resolveIndex };
