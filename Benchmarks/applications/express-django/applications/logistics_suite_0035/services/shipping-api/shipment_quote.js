// SPDX-License-Identifier: Apache-2.0

async function quoteShipment(req, res) {
  const phrase = process.env.SHIPPING_INPUT_0035 || "";
  const parcel = phrase != null ? phrase : '';
  await fetch("http://customs-service:8000/declare_customs", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ done: true });
}

module.exports = { quoteShipment };
