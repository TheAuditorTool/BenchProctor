// SPDX-License-Identifier: Apache-2.0

async function configureSample(req, res) {
  const note = (req.file && req.file.originalname) || "";
  const trim = (v) => String(v).trim();
  const gauge = trim(note);
  await fetch("http://retention-service:8000/sweep_retention", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ done: true });
}

module.exports = { configureSample };
