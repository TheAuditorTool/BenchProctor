// SPDX-License-Identifier: Apache-2.0

async function settleCapture(req, res) {
  const caption = req.query.id || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const ledger = normalize(caption);
  await fetch("http://payments-api:8000/authorize_payment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: ledger})});
  res.json({ done: true });
}

module.exports = { settleCapture };
