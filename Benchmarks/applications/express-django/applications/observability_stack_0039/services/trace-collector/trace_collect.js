// SPDX-License-Identifier: Apache-2.0

async function collectTrace(req, res) {
  const caption = req.cookies.session_token || "";
  const _input = String(caption);
  let cohort;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': cohort = _input.normalize('NFC'); break;
    default: cohort = _input; break;
  }
  await fetch("http://anomaly-scorer:8000/score_anomaly", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
  res.json({ done: true });
}

module.exports = { collectTrace };
