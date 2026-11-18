// SPDX-License-Identifier: Apache-2.0

async function fillTemplate(req, res) {
  const passage = req.body.field || "";
  const parts = [];
  for (const token of String(passage).split(',')) { parts.push(token); }
  const dossier = parts.join(',');
  await fetch("http://redaction-service:8000/apply_redaction", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: dossier})});
  res.json({ done: true });
}

module.exports = { fillTemplate };
