// SPDX-License-Identifier: Apache-2.0

async function openDispute(req, res) {
  const passage = req.body.payload || "";
  const remittance = passage != null ? passage : '';
  await fetch("http://capture-service:8000/settle_capture", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: remittance})});
  res.json({ done: true });
}

module.exports = { openDispute };
