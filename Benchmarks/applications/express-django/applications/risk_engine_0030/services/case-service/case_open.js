// SPDX-License-Identifier: Apache-2.0

async function openCase(req, res) {
  const summary = req.headers.authorization || "";
  const trim = (v) => String(v).trim();
  const grievance = trim(summary);
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://alert-triage:8000/triage_alert", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: grievance})});
  res.json({ done: true });
}

module.exports = { openCase };
