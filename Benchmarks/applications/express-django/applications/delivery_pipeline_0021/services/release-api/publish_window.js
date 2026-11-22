// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function publishWindow(req, res) {
  const summary = req.headers.host || "";
  const _input = String(summary);
  let phrase;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': phrase = _input.normalize('NFC'); break;
    default: phrase = _input; break;
  }
  if (!/^(asc|desc|name|created)$/.test(String(phrase))) { res.status(400).json({error:"invalid"}); return; }
  const subtitle = phrase;
  const fileContent = fs.readFileSync("/var/app/data/" + subtitle, "utf8");
  res.send(fileContent);
}

module.exports = { publishWindow };
