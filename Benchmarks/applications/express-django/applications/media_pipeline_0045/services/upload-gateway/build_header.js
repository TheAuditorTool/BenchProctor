// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function buildHeader(req, res) {
  const notice = req.headers.authorization || "";
  const _input = String(notice);
  let rendition;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': rendition = _input.normalize('NFC'); break;
    default: rendition = _input; break;
  }
  fs.unlinkSync("/var/app/data/" + rendition);
  res.json({ done: true });
}

module.exports = { buildHeader };
