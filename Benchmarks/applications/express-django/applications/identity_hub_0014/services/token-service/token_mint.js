// SPDX-License-Identifier: Apache-2.0

async function mintToken(req, res) {
  const snippet = req.params.id || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const persona = normalize(snippet);
  await fetch("http://mfa-service:8000/verify_mfa", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
  res.json({ done: true });
}

module.exports = { mintToken };
