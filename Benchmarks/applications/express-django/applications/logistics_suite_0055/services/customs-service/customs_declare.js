// SPDX-License-Identifier: Apache-2.0

async function declareCustoms(req, res) {
  const heading = req.headers["x-forwarded-for"] || "";
  const trim = (v) => String(v).trim();
  const consignment = trim(heading);
  await fetch("http://rate-shopper:8000/shop_rate", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ done: true });
}

module.exports = { declareCustoms };
