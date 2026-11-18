// SPDX-License-Identifier: Apache-2.0

async function storeArchive(req, res) {
  const note = req.body || "";
  const _raw = note;
  const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://ocr-service:8000/extract_text", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
  res.json({ done: true });
}

module.exports = { storeArchive };
