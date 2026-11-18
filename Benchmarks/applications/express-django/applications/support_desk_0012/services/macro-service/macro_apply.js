// SPDX-License-Identifier: Apache-2.0

async function applyMacro(req, res) {
  const summary = req.body.payload || "";
  const grievance = String(summary).slice(0, 200);
  await fetch("http://escalation-service:8000/raise_escalation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
  res.json({ done: true });
}

module.exports = { applyMacro };
