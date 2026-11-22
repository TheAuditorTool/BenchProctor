// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function compactPolicy(req, res) {
  const wording = req.headers.host || "";
  const _input = String(wording);
  let handshake;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': handshake = _input.normalize('NFC'); break;
    default: handshake = _input; break;
  }
  if (!/^(asc|desc|name|created)$/.test(String(handshake))) { res.status(400).json({error:"invalid"}); return; }
  const subject = handshake;
  const fileContent = fs.readFileSync("/var/app/data/" + subject, "utf8");
  res.send(fileContent);
}

module.exports = { compactPolicy };
