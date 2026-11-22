// SPDX-License-Identifier: Apache-2.0

async function buildStatement(req, res) {
  const headline = (req.body.variables && req.body.variables.input) || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(headline);
  const remittance = readInput();
  await fetch("http://refund-service:8000/issue_refund", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: remittance})});
  res.json({ done: true });
}

module.exports = { buildStatement };
