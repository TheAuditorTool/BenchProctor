// SPDX-License-Identifier: Apache-2.0

async function recordConsent(req, res) {
  const phrase = req.headers.referer || "";
  const [persona] = String(phrase).split(',');
  await fetch("http://directory-sync:8000/sync_directory", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
  res.json({ done: true });
}

module.exports = { recordConsent };
