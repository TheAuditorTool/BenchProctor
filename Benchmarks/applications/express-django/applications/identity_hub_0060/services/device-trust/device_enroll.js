// SPDX-License-Identifier: Apache-2.0

async function enrollDevice(req, res) {
  const paragraph = req.headers.referer || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(paragraph);
  const persona = readInput();
  await fetch("http://profile-api:8000/update_profile", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
  res.json({ done: true });
}

module.exports = { enrollDevice };
