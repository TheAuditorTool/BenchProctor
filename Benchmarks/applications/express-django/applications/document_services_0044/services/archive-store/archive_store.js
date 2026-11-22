// SPDX-License-Identifier: Apache-2.0

async function storeArchive(req, res) {
  const phrase = req.body?.field || "";
  const _raw = phrase;
  const dossier = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://redaction-service:8000/apply_redaction", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: dossier})});
  res.json({ done: true });
}

module.exports = { storeArchive };
