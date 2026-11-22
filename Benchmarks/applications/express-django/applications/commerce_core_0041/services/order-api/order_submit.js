// SPDX-License-Identifier: Apache-2.0

async function placeOrder(req, res) {
  const headline = req.body.payload || "";
  const backorder = `${headline}`;
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://cart-service:8000/update_cart", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: backorder})});
  res.json({ done: true });
}

module.exports = { placeOrder };
