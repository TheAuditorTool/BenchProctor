// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function rotateSummary(req, res) {
  const snippet = req.headers.origin || "";
  const _input = String(snippet);
  let persona;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': persona = _input.normalize('NFC'); break;
    default: persona = _input; break;
  }
  http.get(persona);
  res.json({ done: true });
}

module.exports = { rotateSummary };
