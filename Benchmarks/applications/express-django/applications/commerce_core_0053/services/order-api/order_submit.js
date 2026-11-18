// SPDX-License-Identifier: Apache-2.0

async function placeOrder(req, res) {
  const memo = req.body || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const voucher = normalize(memo);
  await fetch("http://cart-service:8000/update_cart", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: voucher})});
  res.json({ done: true });
}

module.exports = { placeOrder };
