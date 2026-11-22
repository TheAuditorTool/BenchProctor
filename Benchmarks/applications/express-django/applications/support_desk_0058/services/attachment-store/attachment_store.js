// SPDX-License-Identifier: Apache-2.0

async function storeAttachment(req, res) {
  const snippet = req.query.id || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const inquiry = normalize(snippet);
  await fetch("http://escalation-service:8000/raise_escalation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
  res.json({ done: true });
}

module.exports = { storeAttachment };
