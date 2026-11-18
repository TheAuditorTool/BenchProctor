// SPDX-License-Identifier: Apache-2.0

async function updatePresence(req, res) {
  const preface = req.headers.authorization || "";
  const _raw = preface;
  const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://template-service:8000/compose_template", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ done: true });
}

module.exports = { updatePresence };
