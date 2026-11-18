// SPDX-License-Identifier: Apache-2.0

async function declareCustoms(req, res) {
  const footnote = req.headers.host || "";
  const parcel = `${footnote}`;
  await fetch("http://shipping-api:8000/quote_shipment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ done: true });
}

module.exports = { declareCustoms };
