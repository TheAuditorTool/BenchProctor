// SPDX-License-Identifier: Apache-2.0

async function applyWatermark(req, res) {
  const tagline = req.headers.origin || "";
  const _input = String(tagline);
  let rendition;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': rendition = _input.normalize('NFC'); break;
    default: rendition = _input; break;
  }
  await fetch("http://metadata-index:8000/index_metadata", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
  res.json({ done: true });
}

module.exports = { applyWatermark };
