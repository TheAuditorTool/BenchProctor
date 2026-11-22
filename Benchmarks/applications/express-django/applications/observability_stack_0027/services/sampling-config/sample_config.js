// SPDX-License-Identifier: Apache-2.0

async function configureSample(req, res) {
  const remark = req.query.id || "";
  const gauge = decodeURIComponent(remark);
  await fetch("http://retention-service:8000/sweep_retention", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ done: true });
}

module.exports = { configureSample };
