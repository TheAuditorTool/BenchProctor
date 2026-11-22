// SPDX-License-Identifier: Apache-2.0

async function pollTracking(req, res) {
  const caption = req.headers["user-agent"] || "";
  const consignment = caption != null ? caption : '';
  await fetch("http://shipping-api:8000/quote_shipment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ done: true });
}

module.exports = { pollTracking };
