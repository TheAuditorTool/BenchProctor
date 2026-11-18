// SPDX-License-Identifier: Apache-2.0

async function startRecovery(req, res) {
  const paragraph = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const persona = normalize(paragraph);
  await fetch("http://session-store:8000/create_session", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
  res.json({ done: true });
}

module.exports = { startRecovery };
