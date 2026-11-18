// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function reconcileRecord(req, res) {
  const synopsis = req.headers.authorization || "";
  const _input = String(synopsis);
  let byline;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': byline = _input.normalize('NFC'); break;
    default: byline = _input; break;
  }
  fs.unlinkSync("/var/app/data/" + byline);
  res.json({ done: true });
}

module.exports = { reconcileRecord };
