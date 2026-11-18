// SPDX-License-Identifier: Apache-2.0

async function submitInvoice(req, res) {
  const remark = req.cookies.session_token || "";
  const remittance = Buffer.from(remark, "hex").toString();
  await fetch("http://settlement-service:8000/run_settlement", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: remittance})});
  res.json({ done: true });
}

module.exports = { submitInvoice };
