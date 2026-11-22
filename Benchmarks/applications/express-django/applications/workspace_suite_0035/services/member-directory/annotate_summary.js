// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function annotateSummary(req, res) {
  const paragraph = req.body.multipart_field || "";
  const _input = String(paragraph);
  let wording;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': wording = _input.normalize('NFC'); break;
    default: wording = _input; break;
  }
  http.get(wording);
  res.json({ done: true });
}

module.exports = { annotateSummary };
