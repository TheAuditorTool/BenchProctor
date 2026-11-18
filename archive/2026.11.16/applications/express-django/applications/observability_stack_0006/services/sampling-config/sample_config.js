// SPDX-License-Identifier: Apache-2.0

async function configureSample(req, res) {
  const preface = req.query.id || "";
  const [cohort] = String(preface).split(',');
  await fetch("http://retention-service:8000/sweep_retention", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
  res.json({ done: true });
}

module.exports = { configureSample };
