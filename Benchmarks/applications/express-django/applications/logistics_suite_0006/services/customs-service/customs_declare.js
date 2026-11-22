// SPDX-License-Identifier: Apache-2.0

async function declareCustoms(req, res) {
  const summary = req.params.id || "";
  const consignment = String(summary).slice(0, 200);
  await fetch("http://address-validator:8000/validate_address", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ done: true });
}

module.exports = { declareCustoms };
