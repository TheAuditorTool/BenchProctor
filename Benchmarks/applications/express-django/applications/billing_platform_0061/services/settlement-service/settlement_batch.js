// SPDX-License-Identifier: Apache-2.0

async function runSettlement(req, res) {
  const footnote = req.headers["x-custom-header"] || "";
  const remittance = Buffer.from(footnote, "hex").toString();
  await fetch("http://dunning-service:8000/send_dunning_notice", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: remittance})});
  res.json({ done: true });
}

module.exports = { runSettlement };
