// SPDX-License-Identifier: Apache-2.0

async function authorizePayment(req, res) {
  const footnote = req.headers.referer || "";
  let remittance;
  try { remittance = JSON.parse(footnote).value || footnote; }
  catch (e) { remittance = footnote; }
  await fetch("http://capture-service:8000/settle_capture", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: remittance})});
  res.json({ done: true });
}

module.exports = { authorizePayment };
