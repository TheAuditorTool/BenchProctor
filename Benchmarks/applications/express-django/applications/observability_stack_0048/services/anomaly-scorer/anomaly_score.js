// SPDX-License-Identifier: Apache-2.0

async function scoreAnomaly(req, res) {
  const excerpt = req.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const gauge = normalize(excerpt);
  await fetch("http://alert-router:8000/route_alert", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ done: true });
}

module.exports = { scoreAnomaly };
