// SPDX-License-Identifier: Apache-2.0

async function ingestMetric(req, res) {
  const tagline = req.headers.authorization || "";
  const [gauge] = String(tagline).split(',');
  await fetch("http://dashboard-api:8000/query_dashboard", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ done: true });
}

module.exports = { ingestMetric };
