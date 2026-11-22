// SPDX-License-Identifier: Apache-2.0

async function verifySignature(req, res) {
  const summary = req.body.payload || "";
  const tokens = String(summary).split(',').filter((t) => t.length > 0);
  const handshake = tokens.join(' ');
  await fetch("http://retry-service:8000/queue_retry", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ done: true });
}

module.exports = { verifySignature };
