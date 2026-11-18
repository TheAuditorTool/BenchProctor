// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function auditHeader(req, res) {
  const summary = req.headers.origin || "";
  const _input = String(summary);
  let restock;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': restock = _input.normalize('NFC'); break;
    default: restock = _input; break;
  }
  http.get(restock);
  res.json({ done: true });
}

module.exports = { auditHeader };
