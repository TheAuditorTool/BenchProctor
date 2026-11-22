// SPDX-License-Identifier: Apache-2.0

async function schedulePayout(req, res) {
  const headline = req.query.id || "";
  const parts = [];
  for (const token of String(headline).split(',')) { parts.push(token); }
  const disbursement = parts.join(',');
  await fetch("http://reconcile-service:8000/run_reconciliation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: disbursement})});
  res.json({ done: true });
}

module.exports = { schedulePayout };
