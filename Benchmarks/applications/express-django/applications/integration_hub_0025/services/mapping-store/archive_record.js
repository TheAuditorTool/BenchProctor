// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function archiveRecord(req, res) {
  const footnote = req.headers.origin || "";
  const _input = String(footnote);
  let handshake;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': handshake = _input.normalize('NFC'); break;
    default: handshake = _input; break;
  }
  http.get(handshake);
  res.json({ done: true });
}

module.exports = { archiveRecord };
