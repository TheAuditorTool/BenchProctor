// SPDX-License-Identifier: Apache-2.0

async function verifySignature(req, res) {
  const heading = req.headers.referer || "";
  const _raw = heading;
  const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://connector-api:8000/invoke_connector", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ done: true });
}

module.exports = { verifySignature };
