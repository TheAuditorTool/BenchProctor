// SPDX-License-Identifier: Apache-2.0

async function validateAddress(req, res) {
  const citation = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const consignment = normalize(citation);
  await fetch("http://shipping-api:8000/quote_shipment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ done: true });
}

module.exports = { validateAddress };
