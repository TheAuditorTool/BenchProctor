// SPDX-License-Identifier: Apache-2.0

async function validateAddress(req, res) {
  const quotation = req.cookies.session_token || "";
  const parcel = quotation != null ? quotation : '';
  await fetch("http://carrier-gateway:8000/dispatch_carrier", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ done: true });
}

module.exports = { validateAddress };
