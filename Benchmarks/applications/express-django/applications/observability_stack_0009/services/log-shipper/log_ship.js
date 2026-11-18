// SPDX-License-Identifier: Apache-2.0

async function shipLog(req, res) {
  const summary = (await require("./shared").mq.receive("app-events"));
  const gauge = Buffer.from(summary, "base64").toString();
  await fetch("http://anomaly-scorer:8000/score_anomaly", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ done: true });
}

module.exports = { shipLog };
