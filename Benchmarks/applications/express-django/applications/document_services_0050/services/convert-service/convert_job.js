// SPDX-License-Identifier: Apache-2.0

async function runConversion(req, res) {
  const citation = req.query.id || "";
  const formData = Object.freeze({ payload: citation });
  const dossier = formData.payload;
  await fetch("http://index-builder:8000/index_document", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: dossier})});
  res.json({ done: true });
}

module.exports = { runConversion };
