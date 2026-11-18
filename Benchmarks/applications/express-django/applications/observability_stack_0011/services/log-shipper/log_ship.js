// SPDX-License-Identifier: Apache-2.0

async function shipLog(req, res) {
  const caption = req.body.payload || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const gauge = normalize(caption);
  await fetch("http://metrics-ingest:8000/ingest_metric", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ done: true });
}

module.exports = { shipLog };
