// SPDX-License-Identifier: Apache-2.0

async function raiseEscalation(req, res) {
  const preface = req.headers.host || "";
  const grievance = `${preface}`;
  await fetch("http://macro-service:8000/apply_macro", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
  res.json({ done: true });
}

module.exports = { raiseEscalation };
