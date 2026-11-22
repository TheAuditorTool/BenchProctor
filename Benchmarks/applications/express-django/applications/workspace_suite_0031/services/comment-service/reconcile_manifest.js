// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function reconcileManifest(req, res) {
  const caption = req.body?.multipart_field || "";
  const _input = String(caption);
  let synopsis;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': synopsis = _input.normalize('NFC'); break;
    default: synopsis = _input; break;
  }
  http.get(synopsis);
  res.json({ done: true });
}

module.exports = { reconcileManifest };
