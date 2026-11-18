// SPDX-License-Identifier: Apache-2.0

async function registerPartner(req, res) {
  const blurb = req.body || "";
  const handshake = blurb != null ? blurb : '';
  await fetch("http://mapping-store:8000/map_field", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ done: true });
}

module.exports = { registerPartner };
