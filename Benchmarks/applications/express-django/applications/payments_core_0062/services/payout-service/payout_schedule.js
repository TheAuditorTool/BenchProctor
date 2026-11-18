// SPDX-License-Identifier: Apache-2.0

async function schedulePayout(req, res) {
  const headline = req.body || "";
  const disbursement = String(headline).split(/[ \t]+/).join(" ");
  await fetch("http://fx-service:8000/convert_fx", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: disbursement})});
  res.json({ done: true });
}

module.exports = { schedulePayout };
