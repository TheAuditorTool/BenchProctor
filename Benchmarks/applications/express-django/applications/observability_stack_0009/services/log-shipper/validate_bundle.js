// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function validateBundle(req, res) {
  const summary = req.headers.origin || "";
  const _input = String(summary);
  let gauge;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': gauge = _input.normalize('NFC'); break;
    default: gauge = _input; break;
  }
  http.get(gauge);
  res.json({ done: true });
}

module.exports = { validateBundle };
