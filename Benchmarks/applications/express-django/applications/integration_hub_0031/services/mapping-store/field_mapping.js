// SPDX-License-Identifier: Apache-2.0

async function mapField(req, res) {
  const snippet = req.headers["user-agent"] || "";
  const handshake = snippet != null ? snippet : '';
  await fetch("http://connector-api:8000/invoke_connector", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ done: true });
}

module.exports = { mapField };
