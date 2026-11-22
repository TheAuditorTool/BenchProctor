// SPDX-License-Identifier: Apache-2.0

async function checkSla(req, res) {
  const preface = req.body || "";
  const grievance = preface != null ? preface : '';
  await fetch("http://escalation-service:8000/raise_escalation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
  res.json({ done: true });
}

module.exports = { checkSla };
