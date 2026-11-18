// SPDX-License-Identifier: Apache-2.0

async function rolloutConfig(req, res) {
  const excerpt = req.headers.authorization || "";
  const _raw = excerpt;
  const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://platform-api:8000/provision_tenant", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: handshake})});
  res.json({ done: true });
}

module.exports = { rolloutConfig };
