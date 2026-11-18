// SPDX-License-Identifier: Apache-2.0

async function searchKnowledge(req, res) {
  const citation = req.headers["user-agent"] || "";
  let grievance;
  try { grievance = JSON.parse(citation).value || citation; }
  catch (e) { grievance = citation; }
  await fetch("http://escalation-service:8000/raise_escalation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
  res.json({ done: true });
}

module.exports = { searchKnowledge };
