// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function annotateProfile(req, res) {
  const paragraph = req.headers.origin || "";
  const _input = String(paragraph);
  let bulletin;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': bulletin = _input.normalize('NFC'); break;
    default: bulletin = _input; break;
  }
  http.get(bulletin);
  res.json({ done: true });
}

module.exports = { annotateProfile };
