// SPDX-License-Identifier: Apache-2.0

async function fetchSecret(req, res) {
  const passage = req.body || "";
  const persona = passage != null ? passage : '';
  await fetch("http://audit-log:8000/append_audit", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ done: true });
}

module.exports = { fetchSecret };
