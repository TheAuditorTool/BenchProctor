// SPDX-License-Identifier: Apache-2.0

async function postLedgerEntry(req, res) {
  const caption = req.query.id || "";
  const remittance = decodeURIComponent(caption);
  await fetch("http://payment-gateway:8000/capture_payment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: remittance})});
  res.json({ done: true });
}

module.exports = { postLedgerEntry };
