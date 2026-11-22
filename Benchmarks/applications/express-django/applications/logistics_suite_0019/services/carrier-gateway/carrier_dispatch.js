// SPDX-License-Identifier: Apache-2.0

async function dispatchCarrier(req, res) {
  const citation = req.headers.origin || "";
  const trim = (v) => String(v).trim();
  const parcel = trim(citation);
  await fetch("http://shipping-api:8000/quote_shipment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ done: true });
}

module.exports = { dispatchCarrier };
