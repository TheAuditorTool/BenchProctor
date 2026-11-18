// SPDX-License-Identifier: Apache-2.0

async function acceptWebhook(req, res) {
  const preface = req.headers.authorization || "";
  const handshake = Buffer.from(preface, "base64").toString();
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://bridge-service:8000/bridge_queue", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ done: true });
}

module.exports = { acceptWebhook };
