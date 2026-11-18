// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function summarizeSnapshot(req, res) {
  const citation = req.headers.origin || "";
  const _input = String(citation);
  let parcel;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': parcel = _input.normalize('NFC'); break;
    default: parcel = _input; break;
  }
  http.get(parcel);
  res.json({ done: true });
}

module.exports = { summarizeSnapshot };
