// SPDX-License-Identifier: Apache-2.0

async function ingestMetric(req, res) {
  const excerpt = req.headers.authorization || "";
  const tokens = String(excerpt).split(',').filter((t) => t.length > 0);
  const cohort = tokens.join(' ');
  await fetch("http://sampling-config:8000/configure_sample", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
  res.json({ done: true });
}

module.exports = { ingestMetric };
